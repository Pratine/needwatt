from django.contrib import admin
from .models import Client, Provider, Tariff_BTN, Tariff_BTE, Tariff_MT


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    fields = ["client_name",
              "client_email",
              "client_nif",
              "client_contract_begin",
              "client_contract_end"]


class ProviderAdmin(admin.ModelAdmin):
    fields = ["provider_name"]


class TariffBTNAdmin(admin.ModelAdmin):
    fields = ["btn_provider",
              "btn_power",
              "btn_cicle",
              "btn_price_day",
              "btn_simple",
              "btn_bi_f_vazio",
              "btn_bi_vazio",
              "btn_tri_ponta",
              "btn_tri_cheias",
              "btn_tri_vazio",
              "btn_tariff_date_start",
              "btn_tariff_date_end"
              ]


class TariffMTAdmin(admin.ModelAdmin):
    fields = ["mt_provider",
              "mt_cicle",
              "mt_tarrif_pontas",
              "mt_tarrif_cheias",
              "mt_tarrif_vazio_normal",
              "mt_tarrif_super_vazio",
              "mt_tariff_date_start",
              "mt_tariff_date_end"]


class TariffBTEAdmin(admin.ModelAdmin):
    fields = ["bte_provider",
              "bte_cicle",
              "bte_tarrif_pontas",
              "bte_tarrif_cheias",
              "bte_tarrif_vazio_normal",
              "bte_tarrif_super_vazio",
              "bte_tariff_date_start",
              "bte_tariff_date_end"]


admin.site.register(Client, ClientAdmin),
admin.site.register(Provider, ProviderAdmin),
admin.site.register(Tariff_BTN, TariffBTNAdmin),
admin.site.register(Tariff_MT, TariffMTAdmin),
admin.site.register(Tariff_BTE, TariffBTEAdmin),
admin.site.site_header = "NeedWatt Admin Page"
