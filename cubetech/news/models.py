from django.db import models
from tinymce.models import HTMLField


class News(models.Model):
    title=models.CharField(max_length=100)

# Create your models here.
