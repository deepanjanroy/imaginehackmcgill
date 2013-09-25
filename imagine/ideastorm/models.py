from django.db import models

# Create your models here.

class Idea(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now=True)