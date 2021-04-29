import datetime
from builtins import str

import django.utils.timezone
from django.db import models


# Create your models here.

# Model for clients:
class Client(models.Model):
    client_name = models.CharField("Nome", max_length=220, default="")
    client_email = models.EmailField("Email", max_length=220, default="")
    client_nif = models.CharField("NIF", max_length=11, default="PT000000000", unique=True)
    client_contract_begin = models.DateField("Data de inicio de contracto", default=django.utils.timezone.now)
    client_contract_end = models.DateField("Data de fim de contracto", default=django.utils.timezone.now)

    def __str__(self):
        return 'Nome: ' + self.client_name + ', NIF: ' + self.client_nif


# Model for provider:
class Provider(models.Model):
    provider_name = models.CharField("Fornecedor", max_length=220, default="")

    def __str__(self):
        return self.provider_name


# Model for tariffBTN:
class Tariff_BTN(models.Model):
    btn_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    BTN_POWER = (
        ('1.15', '1.15'),
        ('3.45', '3.45'),
        ('4.6', '4.6'),
        ('5.75', '5.75'),
        ('6.9', '6.9'),
        ('10.35', '10.35'),
        ('13.8', '13.8'),
        ('17.25', '17.25'),
        ('20.7', '20.7'),
        ('27.6', '27.6'),
        ('34.5', '34.5'),
        ('41.40', '41.40')
    )
    btn_power = models.CharField("Potencia contratada", max_length=5, choices=BTN_POWER, default="")

    BTN_CICLE = (
        ('Simp', 'Simples'),
        ('Bi-H', 'Bi-Horario'),
        ('Tri-H', 'Tri-Horario')
    )
    btn_cicle = models.CharField("Ciclo", max_length=5, choices=BTN_CICLE, default="")

    btn_price_day = models.FloatField("Preço/dia", default=0.0)
    btn_simple = models.FloatField("Tarifa Simple", default=0.0)
    btn_bi_f_vazio = models.FloatField("Tarrifa Fora Vazio", default=0.0)
    btn_bi_vazio = models.FloatField("Tarrifa Vazio", default=0.0)
    btn_tri_ponta = models.FloatField("Tarrifa Pontas", default=0.0)
    btn_tri_cheias = models.FloatField("Tarrifa Cheias", default=0.0)
    btn_tri_vazio = models.FloatField("Tarrifa Vazio", default=0.0)

    btn_tariff_date_start = models.DateField("Data de inicio", default=django.utils.timezone.now)
    btn_tariff_date_end = models.DateField("Data de fim", default=django.utils.timezone.now)


# Model for tariff_BTE
class Tariff_BTE(models.Model):
    bte_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    BTE_CICLE = (
        ('Diario', 'Diario'),
        ('Semanal', 'Semanal')
    )
    bte_cicle = models.CharField("Ciclo", max_length=10, choices=BTE_CICLE, default="")
    bte_tarrif_pontas = models.FloatField("Horas Ponta", default=0.0)
    bte_tarrif_cheias = models.FloatField("Horas Cheias", default=0.0)
    bte_tarrif_vazio_normal = models.FloatField("Horas de vazio normal", default=0.0)
    bte_tarrif_super_vazio = models.FloatField("Horas de super vazio", default=0.0)

    bte_tarrif_pontas_c_redes = models.FloatField("Horas Ponta com Redes", default=0.0)
    bte_tarrif_cheias_c_redes = models.FloatField("Horas Cheias com Redes", default=0.0)
    bte_tarrif_vazio_normal_c_redes = models.FloatField("Horas de vazio normal com Redes", default=0.0)
    bte_tarrif_super_vazio_c_redes = models.FloatField("Horas de super vazio com Redes", default=0.0)

    bte_tariff_date_start = models.DateField("Data de inicio", default=django.utils.timezone.now)
    bte_tariff_date_end = models.DateField("Data de fim", default=django.utils.timezone.now)


class Tariff_MT(models.Model):
    mt_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    MT_CICLE = (
        ('c/f', 'semanal c/feriados'),
        ('o/c', 'semanal c/opcao cliente')
    )
    mt_cicle = models.CharField("Ciclo", max_length=3, choices=MT_CICLE, default="")

    mt_tarrif_pontas = models.FloatField("Horas Ponta", default=0.0)
    mt_tarrif_cheias = models.FloatField("Horas Cheias", default=0.0)
    mt_tarrif_vazio_normal = models.FloatField("Horas de vazio normal", default=0.0)
    mt_tarrif_super_vazio = models.FloatField("Horas de super vazio", default=0.0)

    mt_tarrif_pontas_c_redes = models.FloatField("Horas Ponta com Redes", default=0.0)
    mt_tarrif_cheias_c_redes = models.FloatField("Horas Cheias com Redes", default=0.0)
    mt_tarrif_vazio_normal_c_redes = models.FloatField("Horas de vazio normal com Redes", default=0.0)
    mt_tarrif_super_vazio_c_redes = models.FloatField("Horas de super vazio com Redes", default=0.0)

    mt_tariff_date_start = models.DateField("Data de inicio", default=django.utils.timezone.now)
    mt_tariff_date_end = models.DateField("Data de fim", default=django.utils.timezone.now)
