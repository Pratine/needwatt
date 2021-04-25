# Generated by Django 3.2 on 2021-04-14 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_contract_begin',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de inicio de contracto'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_contract_end',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de fim de contracto'),
        ),
        migrations.AlterField(
            model_name='tariffbtn',
            name='btn_tariff_date_end',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de fim de contracto'),
        ),
        migrations.AlterField(
            model_name='tariffbtn',
            name='btn_tariff_date_start',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de inicio de contracto'),
        ),
    ]
