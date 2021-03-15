from django.db import models
from phone_field import PhoneField
from django.core.validators import MinLengthValidator, int_list_validator

class registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    contact = models.CharField(verbose_name="Phone number", max_length=10,
    validators=[int_list_validator(sep=''),MinLengthValidator(10),], 
    unique=True)

class addfurniture(models.Model):
    fname=models.CharField(max_length=50)
    fdetail=models.CharField(max_length=50)
    fprice=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    scontact=models.CharField(max_length=50)

    
    
