from re import T
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True,blank=True)
    addres = models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return str(self.user)