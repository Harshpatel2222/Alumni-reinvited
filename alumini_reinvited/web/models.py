from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False)
    bio = models.TextField(max_length=500, null=True)
    email = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.name
