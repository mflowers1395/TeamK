from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    CWID = models.CharField(max_length=9)
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.firstname + " " + self.lastname

