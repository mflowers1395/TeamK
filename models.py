from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    CWID = models.CharField(max_length = 9)