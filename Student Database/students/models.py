from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    CWID = models.CharField(max_length=9)
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.firstname + " " + self.lastname


class Textbook(models.Model):
    booktitle = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    ISBN = models.IntegerField()

    def __str__(self):
        return self.booktitle


