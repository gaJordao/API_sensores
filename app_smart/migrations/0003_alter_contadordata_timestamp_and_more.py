# Generated by Django 5.0.6 on 2024-05-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0002_rename_mac_address_sensor_mac_adress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contadordata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='umidadedata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
