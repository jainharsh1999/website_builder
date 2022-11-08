from django.db import models

# Create your models here.
class employee(models.Model):
    Email = models.CharField(max_length=100, null=True, blank=False)
    password = models.IntegerField(max_length=255, null=True, blank=False)
    city = models.CharField(max_length=100, null=True, blank=False)
    state = models.CharField(max_length=255, null=True, blank=False)
    address = models.CharField(max_length=100, null=True, blank=False)
    pincode = models.IntegerField(max_length=255, null=True, blank=False)