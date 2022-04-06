from django.db import models
from django.contrib.auth.models import User

class Textbook(models.Model):
    booktitle = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=30)
    isbn = models.CharField('ISBN', max_length=13)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.booktitle
