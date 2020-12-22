from django.db import models
from accounts.models import User

# Create your models here.

class Catalogue(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=0)

    # Order the catalogue be name
    class Meta:
        ordering = ['name']


class Book(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    catalogue = models.ForeignKey(Catalogue, on_delete = models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, default=0)

    # Order books by ascending date created
    class Meta:
        ordering = ['-created']