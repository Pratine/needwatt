# Generated by Django 3.2 on 2021-04-16 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210416_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tariff_bte',
            old_name='mt_bte_cicle',
            new_name='bte_cicle',
        ),
        migrations.RenameField(
            model_name='tariff_bte',
            old_name='mt_bte_tariff_date_end',
            new_name='bte_tariff_date_end',
        ),
        migrations.RenameField(
            model_name='tariff_bte',
            old_name='mt_bte_tariff_date_start',
            new_name='bte_tariff_date_start',
        ),
    ]