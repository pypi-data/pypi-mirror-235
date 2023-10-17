from django.db import transaction
from django.db.models import signals
from django.core.exceptions import MiddlewareNotUsed, PermissionDenied

from ipam.models import IPAddress
from extras.plugins import get_plugin_config
from netbox_dns.models import Zone, Record, RecordTypeChoices
from utilities.exceptions import PermissionsViolation, AbortRequest
from utilities.permissions import resolve_permission


class Action:
    def __init__(self, request):
        self.request = request

    #
    # Check permission to create DNS record before IP address creation
    # NB: If IP address is created *before* DNS record is allowed it's too late
    # → permission check must be done at pre-save, and an exception
    # must be raised to prevent IP creation.
    #
    def pre_save(self, sender, **kwargs):
        if kwargs.get("update_fields"):
            return

        ip_address = kwargs.get("instance")
        name = ip_address.custom_field_data.get("ipaddress_dns_record_name")
        zone_id = ip_address.custom_field_data.get("ipaddress_dns_zone_id")

        # Handle new IPAddress objects only; name and zone must both be defined
        if ip_address.id is None and name is not None and zone_id is not None:
            zone = Zone.objects.get(id=zone_id)
            type = (
                RecordTypeChoices.AAAA
                if ip_address.family == 6
                else RecordTypeChoices.A
            )
            value = str(ip_address.address.ip)

            # Create a DNS record *without saving* in order to check permissions
            record = Record(name=name, zone=zone, type=type, value=value)
            user = self.request.user
            check_record_permission(user, record, "netbox_dns.add_record")

    #
    # Handle DNS record operation after IPAddress has been created or modified
    #
    def post_save(self, sender, **kwargs):
        # Do not process specific field update (eg. dns_hostname modify)
        if kwargs.get("update_fields"):
            return

        ip_address = kwargs.get("instance")
        user = self.request.user
        name = ip_address.custom_field_data.get("ipaddress_dns_record_name")
        zone_id = ip_address.custom_field_data.get("ipaddress_dns_zone_id")
        zone = Zone.objects.get(id=zone_id) if zone_id is not None else None

        # Clear the other field if one is empty, which is inconsistent
        if name is None:
            zone = None
        elif zone is None:
            name = None

        # Delete the DNS record because name and zone have been removed
        if zone is None:
            # Find the record pointing to this IP Address
            for record in ip_address.netbox_dns_records.all():
                # If permission ok, clear all fields related to DNS
                check_record_permission(user, record, "netbox_dns.delete_record")

                ip_address.dns_name = ""
                ip_address.custom_field_data["ipaddress_dns_record_name"] = ""
                ip_address.save(update_fields=["custom_field_data", "dns_name"])

                record.delete()

        # Modify or add the DNS record
        else:
            type = (
                RecordTypeChoices.AAAA
                if ip_address.family == 6
                else RecordTypeChoices.A
            )

            # If DNS record already point to this IP, modify it
            record = ip_address.netbox_dns_records.first()
            if record is not None:
                record.name = name
                record.zone = zone
                record.value = str(ip_address.address.ip)
                record.type = type

                check_record_permission(user, record, "netbox_dns.change_record")
                record.save()

            else:
                # Create a new record
                record = Record(
                    name=name,
                    zone=zone,
                    type=type,
                    value=str(ip_address.address.ip),
                    ipam_ip_address=ip_address,
                    managed=True,
                )

                check_record_permission(
                    user, record, "netbox_dns.add_record", commit=True
                )

            # Update the dns_name field with FQDN
            ip_address.dns_name = record.fqdn.rstrip(".")
            ip_address.save(update_fields=["dns_name"])

    #
    # Delete DNS record before deleting IP address
    #
    def pre_delete(self, sender, **kwargs):
        ip_address = kwargs.get("instance")

        for record in ip_address.netbox_dns_records.all():
            user = self.request.user
            check_record_permission(user, record, "netbox_dns.delete_record")

            record.delete()


#
# Filter through permissions. Simulate adding the record in the "add" case.
# NB: Side-effect if "commit" is set to True → the DNS record is created.
# This is necessary to avoid the cascading effects of PTR creation.
#
def check_record_permission(user, record, perm, commit=False):
    # Check that the user has been granted the required permission(s).
    action = resolve_permission(perm)[1]

    if not user.has_perm(perm):
        raise PermissionDenied()

    try:
        with transaction.atomic():
            # Save record when adding
            # Rollback is done at the end of the transaction, unless committed

            if action == "add":
                record.save()

            # Update the view's QuerySet to filter only the permitted objects
            queryset = Record.objects.restrict(user, action)
            # Check that record conforms to permissions
            # → must be included in the restricted queryset
            if not queryset.filter(pk=record.pk).exists():
                raise PermissionDenied()

            if not commit:
                raise AbortRequest("Normal Exit")

    # Catch "Normal Exit" without modification, rollback transaction
    except AbortRequest as exc:
        pass

    except Exception as exc:
        raise exc


class IpamCouplingMiddleware:
    def __init__(self, get_response):
        if not get_plugin_config("netbox_dns", "feature_ipam_coupling"):
            raise MiddlewareNotUsed

        self.get_response = get_response

    def __call__(self, request):
        # connect signals to actions
        action = Action(request)
        connections = [
            (signals.pre_save, action.pre_save),
            (signals.post_save, action.post_save),
            (signals.pre_delete, action.pre_delete),
        ]
        for signal, receiver in connections:
            signal.connect(receiver, sender=IPAddress)

        response = self.get_response(request)

        for signal, receiver in connections:
            signal.disconnect(receiver)

        return response
