# Generated by Django 5.0.6 on 2025-01-17 20:23

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation', '0005_bloodbank_phone_number_alter_blooddonor_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbank',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='blooddonor',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
