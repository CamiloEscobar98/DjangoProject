from django.db import models

# Create your models here.
class Vulnerability(models.Model):
    code = models.TextField(unique=True)