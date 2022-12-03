# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Hangar(models.Model):
    hangar_id = models.AutoField(db_column='Hangar_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', blank=True, null=True, max_length=200)  # Field name made lowercase.
    city = models.CharField(db_column='City', blank=True, null=True, max_length=200)  # Field name made lowercase.
    address = models.CharField(db_column='Address', blank=True, null=True, max_length=200)  # Field name made lowercase.
    dimension = models.CharField(db_column='Dimension', blank=True, null=True, max_length=200)  # Field name made lowercase.
    enclosure_type = models.CharField(db_column='Enclosure_Type', blank=True, null=True, max_length=200)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    available_duration = models.IntegerField(db_column='Available_Duration', blank=True, null=True)  # Field name made lowercase.
    heating = models.CharField(db_column='Heating', blank=True, null=True, max_length=200)  # Field name made lowercase.
    water_and_electricity = models.CharField(db_column='Water_and_Electricity', blank=True, null=True, max_length=200)  # Field name made lowercase.
    technician = models.CharField(db_column='Technician', blank=True, null=True, max_length=200)  # Field name made lowercase.
    rented_by = models.ForeignKey('User', models.DO_NOTHING, related_name='rented_by', db_column='Rented_By', blank=True, null=True)  # Field name made lowercase.
    owned_by = models.ForeignKey('User', models.DO_NOTHING, related_name='owned_by', db_column='Owned_By', blank=True, null=True, max_length=200)  # Field name made lowercase.

    class Meta:
        db_table = 'Hangar'


class Location(models.Model):
    address = models.CharField(db_column='Address', primary_key=True, max_length=200)  # Field name made lowercase.
    city = models.CharField(db_column='City', unique=True,max_length=200)  # Field name made lowercase.
    zip_code = models.IntegerField(db_column='Zip_Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'Location'


class RentalPeriod(models.Model):
    hangar = models.OneToOneField(Hangar, models.DO_NOTHING, db_column='Hangar_ID', primary_key=True)  # Field name made lowercase.
    rentee_user = models.ForeignKey('User', models.DO_NOTHING, db_column='Rentee_User')  # Field name made lowercase.
    rental_duration = models.IntegerField(db_column='Rental_Duration', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'Rental_Period'


class Role(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=200)  # Field name made lowercase.

    class Meta:

        db_table = 'Role'


class User(models.Model):
    user_id = models.AutoField( db_column='User_ID', primary_key=True)  # Field name made lowercase.
    password = models.CharField(max_length=200, blank=False, db_column='Password')
    email =  models.CharField(max_length=200, blank=False, db_column='email')
    first_name = models.CharField(db_column='First_Name', blank=True, null=True, max_length=200)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', blank=True, null=True, max_length=200)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200)  # Field name made lowercase.
    city = models.CharField(db_column='City', unique=False, max_length=200)  # Field name made lowercase.

    class Meta:

        db_table = 'User'
def save(self, *args, **kwargs):
        self.user_id = self.user_id + 1
        super().save(*args, **kwargs)