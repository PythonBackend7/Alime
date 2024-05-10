from django.db import models


# Create your models here.
class Contact_Info(models.Model):
    email = models.EmailField()
    location = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
