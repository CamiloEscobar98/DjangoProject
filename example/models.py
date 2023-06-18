from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class Vulnerability(models.Model):
    code = models.TextField(unique=True)