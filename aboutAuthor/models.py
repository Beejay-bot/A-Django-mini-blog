from django.db import models

# Create your models here.


class Author(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=None, blank=False, null=True, editable=True)
