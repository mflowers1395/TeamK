from django.db import models

class Textbook(models.Model):
    booktitle = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=30)
    isbn = models.CharField('ISBN', max_length=13)
    poster = models.CharField('Poster', max_length=30)

    def __str__(self):
        return self.booktitle
