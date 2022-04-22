from django.db import models
from django.contrib.auth.models import User

class Textbook(models.Model):
    booktitle = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=30)
    isbn = models.CharField('ISBN', max_length=13)
    price = models.FloatField('Price', max_length=8, default=10)
    

    def __str__(self):
        return self.booktitle

class Order(models.Model):
	product = models.ForeignKey(Textbook, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.booktitle
