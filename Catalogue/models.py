<<<<<<< HEAD
from django.db import models

class Textbook(models.Model):
    booktitle = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=30)
    isbn = models.CharField('ISBN', max_length=13)

    def __str__(self):
        return self.booktitle
=======
from django.db import models

class Textbook(models.Model):
    booktitle = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=30)
    isbn = models.CharField('ISBN', max_length=13)
    poster = models.CharField('Poster', max_length=30)

    def __str__(self):
        return self.booktitle
>>>>>>> 911aaed20769ad750d24497adb73ca333f370dac
