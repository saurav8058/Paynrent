from django.db import models


# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=70, blank=False, default='')
    description= models.CharField(max_length=150, blank=False, default='')
    icon=models.ImageField(upload_to='static/')
class SubCategory(models.Model):
    category_id = models.CharField(max_length=70, blank=False, default='')
    company_name = models.CharField(max_length=70, blank=False, default='')
    subcategory_name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=150, blank=False, default='')
    icon = models.ImageField(upload_to='static/')

class Vehicle(models.Model):
    category_id = models.CharField(max_length=100, blank=False, default='')
    subcategory_id = models.CharField(max_length=100, blank=False, default='')
    model_year = models.CharField(max_length=170, blank=False, default='')
    variant = models.CharField(max_length=170, blank=False, default='')
    price = models.CharField(max_length=170, blank=False, default='')
    insured = models.CharField(max_length=70, blank=False, default='')
    registration_no = models.CharField(max_length=170, blank=False, default='')
    owner_name = models.CharField(max_length=170, blank=False, default='')
    mobile_no = models.CharField(max_length=170, blank=False, default='')
    color = models.CharField(max_length=170, blank=False, default='')
    fuel_type = models.CharField(max_length=170, blank=False, default='')
    no_of_seats = models.CharField(max_length=170, blank=False, default='')
    transmission_type = models.CharField(max_length=170, blank=False, default='')
    icon = models.ImageField(upload_to='static/')    
class Administrator(models.Model):
    adminname = models.CharField(max_length=70, blank=False, default='')
    mobileno= models.CharField(max_length=15, blank=False, default='')
    emailid= models.CharField(max_length=150, blank=False, default='')
    password= models.CharField(max_length=150, blank=False, default='')


