# Generated by Django 5.0.3 on 2024-03-14 06:49

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('bank_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('blood_quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BloodDonor',
            fields=[
                ('donor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('blood_group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('P', 'Prefer Not To Say')], max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255, null=True)),
                ('surname', models.CharField(max_length=255)),
                ('date_of_Birth', models.DateField(default=django.utils.timezone.now)),
                ('blood_group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('P', 'Prefer Not To Say')], max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('name_of_next_of_kin', models.CharField(max_length=255)),
                ('phone_number_of_next_of_kin', models.CharField(max_length=20)),
                ('medical_Conditions', models.TextField()),
            ],
        ),
    ]
