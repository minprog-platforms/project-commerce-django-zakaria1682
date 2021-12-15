from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, IntegerField
from django.db import models
from django.forms import ModelForm
from django.db.models.fields.related import *


class User(AbstractUser):
    pass

class Create_listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    initial_bid = models.IntegerField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    

class Listing_Form(ModelForm):
    class Meta:
        model = Create_listing
        fields = ('title', 'description', 'initial_bid') 
    