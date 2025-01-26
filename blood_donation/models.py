from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

gender = (('M', 'Male'), ('F', 'Female'), ('P', 'Prefer Not To Say'))
blood_group = (("A", "A"), ("B", "B"), ("AB", "AB"), ("O", "O"))


# Creating the table Patient
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255)
    date_of_Birth = models.DateField(default="2000-30-12")
    blood_group = models.CharField(max_length=255, choices=blood_group)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=gender)
    phone_number = PhoneNumberField()
    email = models.EmailField(null=True)
    name_of_next_of_kin = models.CharField(max_length=255)
    phone_number_of_next_of_kin = models.CharField(max_length=20)
    medical_Conditions = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.surname}"


# Creating the table Blood Bank
class BloodBank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    blood_quantity_in_pints = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    address = models.CharField(max_length=255)
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"{self.name}"


# Creating the table Blood Donor
class BloodDonor(models.Model):
    donor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=255, choices=blood_group)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=gender)
    phone_number = PhoneNumberField()
    date_of_donation = models.DateField(auto_now=True)
    eligible_to_donate = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    def is_eligible(self):
        import datetime
        if (datetime.date.today() - self.date_of_donation) < datetime.timedelta(days=0.01):
            self.eligible_to_donate = False