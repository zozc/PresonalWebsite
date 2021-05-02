from django.db import models

# Create your models here.

class Product (models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price       = models.IntegerField()
    featured    = models.BooleanField(default=False)