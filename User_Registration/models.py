from django.db import models
from Catalogue.models import Textbook

class WishList(models.Model):

    username = models.CharField(max_length=50)
    textbooks = models.ManyToManyField(Textbook, related_name="wishlists")

    def __str__(self):
        return self.username
