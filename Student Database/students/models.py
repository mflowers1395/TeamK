from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    user_name = models.CharField(max_length = 20)
    CWID = models.CharField(max_length = 9)

    def __str__(self) -> str:
        return self.user_name + " / " + self.CWID
