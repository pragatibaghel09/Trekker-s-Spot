# from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Registration(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=200)
    mo_num = models.IntegerField()
    email = models.EmailField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    
    def __str__(self):
        return self.full_name

    
class Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    card_type= models.CharField(max_length=100)
    mo_num= models.CharField(max_length=200)
    acnum = models.IntegerField()
    card_num = models.IntegerField()
    cvv = models.IntegerField() 
    
    def __str__(self):
        return self.full_name   
    


class Feedback(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Trektrip = models.CharField(max_length=100,blank=True)
    suggestions = models.TextField(max_length=400,default="0")
    
    def __str__(self):
        return self.Email