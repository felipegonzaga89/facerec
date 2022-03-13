from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User



# Create your models here.
class UserProfile(models.Model):
    user=models.CharField(max_length=30)
    photo = models.ImageField(upload_to='clients_photos', blank=True)
    fr = models.CharField(max_length=100000)



    
