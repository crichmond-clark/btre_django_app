from django.db import models
from datetime import datetime

# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    seller_of_month = models.BooleanField(default=False)
    hire_date = models.DateTimeField(datetime.now)

    def __str__(self):
        return self.name
