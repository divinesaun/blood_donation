# Generated by Django 5.0.3 on 2024-03-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation', '0003_rename_blood_quantity_bloodbank_blood_quantity_in_pints'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonor',
            name='eligible_to_donate',
            field=models.BooleanField(default=True),
        ),
    ]
