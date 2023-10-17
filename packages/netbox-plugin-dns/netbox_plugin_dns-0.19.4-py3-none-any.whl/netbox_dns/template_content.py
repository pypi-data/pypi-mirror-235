from django.db.models.functions import Length

from extras.plugins.utils import get_plugin_config
from extras.plugins import PluginTemplateExtension

from netbox_dns.models import Record, RecordTypeChoices, Zone, View, NameServer
from netbox_dns.tables import RelatedRecordTable, RelatedZoneTable


class RelatedDNSRecords(PluginTemplateExtension):
    model = "ipam.ipaddress"

    def right_page(self):
        obj = self.context.get("object")

        address_records = Record.objects.filter(
            ip_address=obj.address.ip,
            type__in=(RecordTypeChoices.A, RecordTypeChoices.AAAA),
        )
        pointer_records = Record.objects.filter(
            ip_address=obj.address.ip, type=RecordTypeChoices.PTR
        )
        address_record_table = RelatedRecordTable(
            data=address_records,
        )
        pointer_record_table = RelatedRecordTable(
            data=pointer_records,
        )

        return self.render(
            "netbox_dns/record/related.html",
            extra_context={
                "related_address_records": address_record_table,
                "related_pointer_records": pointer_record_table,
            },
        )


class RelatedDNSPointerZones(PluginTemplateExtension):
    model = "ipam.prefix"

    def full_width_page(self):
        obj = self.context.get("object")

        pointer_zones = (
            Zone.objects.filter(
                arpa_network__net_contains_or_equals=obj.prefix
            ).order_by(Length("name").desc())[:1]
            | Zone.objects.filter(arpa_network__net_contained=obj.prefix)
        ).order_by("name")

        pointer_zone_table = RelatedZoneTable(
            data=pointer_zones,
        )

        return self.render(
            "netbox_dns/zone/related.html",
            extra_context={
                "related_pointer_zones": pointer_zone_table,
            },
        )


class RelatedDNSObjects(PluginTemplateExtension):
    model = "tenancy.tenant"

    def left_page(self):
        obj = self.context.get("object")
        request = self.context.get("request")

        related_dns_models = (
            (
                View.objects.restrict(request.user, "view").filter(tenant=obj),
                "tenant_id",
            ),
            (
                NameServer.objects.restrict(request.user, "view").filter(tenant=obj),
                "tenant_id",
            ),
            (
                Zone.objects.restrict(request.user, "view").filter(tenant=obj),
                "tenant_id",
            ),
            (
                Record.objects.restrict(request.user, "view").filter(tenant=obj),
                "tenant_id",
            ),
        )

        return self.render(
            "netbox_dns/related_dns_objects.html",
            extra_context={
                "related_dns_models": related_dns_models,
            },
        )


template_extensions = [RelatedDNSObjects]
if get_plugin_config("netbox_dns", "feature_ipam_integration"):
    template_extensions += [RelatedDNSRecords, RelatedDNSPointerZones]
