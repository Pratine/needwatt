# Generated by Django 3.2 on 2021-04-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210416_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff_btn',
            name='btn_price_day',
            field=models.FloatField(default=0.0, verbose_name='Preço/dia'),
        ),
    ]
