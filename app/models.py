from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)
    city = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)

    