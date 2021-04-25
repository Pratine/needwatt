import sys
from operator import xor

from . import models
from .models import Tariff_BTN, Tariff_BTE, Tariff_MT
import django.utils.timezone

# value for IVA
IVA_value = 0.23


def percentage_difference_calculator(value_0, value_1):
    return ((value_0 - value_1) / ((value_0 + value_1) / 2)) * 100


# Simulations for btn -- Start --
def simulation_btn_simple(hired_power, n_days, price_p_month):
    lowest_value = sys.float_info.max

    for x in Tariff_BTN.objects.all():
        value = 0.0
        if x.btn_power == hired_power and django.utils.timezone.now > x.btn_tariff_date_start and django.utils.timezone.now < x.btn_tariff_date_end:
            value = (n_days * x.btn_price_day) + (
                    n_days * x.btn_simple)
        if lowest_value > value:
            lowest_value = value

    final_value = lowest_value + (lowest_value * IVA_value)

    return percentage_difference_calculator(price_p_month, final_value)


def simulation_btn_bi_hor(hired_power, n_days, price_p_month):
    lowest_value = sys.float_info.max
    for x in Tariff_BTN.objects.all():
        value = 0.0
        if x.btn_power == hired_power and django.utils.timezone.now > x.btn_tariff_date_start and django.utils.timezone.now > x.btn_tariff_date_end:
            value = (n_days * x.btn_price_day) + (
                    n_days * x.btn_bi_f_vazio) + (
                            n_days * x.btn_bi_vazio)
        if lowest_value > value:
            lowest_value = value

    final_value = lowest_value + (lowest_value * IVA_value)

    return percentage_difference_calculator(price_p_month, final_value)


def simulation_btn_tri_hor(hired_power, n_days, price_p_month):
    lowest_value = sys.float_info.max
    for x in Tariff_BTN.objects.all():
        value = 0.0
        if x.btn_power == hired_power and django.utils.timezone.now > x.btn_tariff_date_start and django.utils.timezone.now > x.btn_tariff_date_end:
            value = (n_days * x.btn_price_day) + (
                    n_days * x.btn_tri_ponta) + (
                            n_days * x.btn_tri_cheias) + (
                            n_days * x.btn_tri_vazio)
        if lowest_value > value:
            lowest_value = value

    final_value = lowest_value + (lowest_value * IVA_value)

    return percentage_difference_calculator(price_p_month, final_value)


# -- End --

# -- Start --
def simulation_mt(power_pontas, power_cheias, power_vazio_normal, power_super_vazio, price_p_month):
    lowest_value = sys.float_info.max
    for x in Tariff_MT.objects.all():
        value = 0.0
        if django.utils.timezone.now > x.mt_tariff_date_start and django.utils.timezone.now > x.mt_tariff_date_end:
            value = (power_pontas * x.mt_tarrif_pontas) + (
                    power_cheias * x.mt_tarrif_cheias) + (
                            power_vazio_normal * x.mt_tarrif_vazio_normal) + (
                            power_super_vazio * x.mt_tarrif_super_vazio)
        if lowest_value > value:
            lowest_value = value

    final_value = lowest_value + (lowest_value * IVA_value)

    return percentage_difference_calculator(price_p_month, final_value)


# -- End --

# -- Start --
def simulation_bte(power_pontas, power_cheias, power_vazio_normal, power_super_vazio, price_p_month):
    lowest_value = sys.float_info.max
    for x in Tariff_BTE.objects.all():
        value = 0.0
        if django.utils.timezone.now > x.bte_tariff_date_start and django.utils.timezone.now > x.bte_tariff_date_end:
            value = (power_pontas * x.bte_tarrif_pontas) + (
                    power_cheias * x.bte_tarrif_cheias) + (
                            power_vazio_normal * x.bte_tarrif_vazio_normal) + (
                            power_super_vazio * x.bte_tarrif_super_vazio)
        if lowest_value > value:
            lowest_value = value

    final_value = lowest_value + (lowest_value * IVA_value)

    return percentage_difference_calculator(price_p_month, final_value)
# -- End --
