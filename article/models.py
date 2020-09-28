from django.db import models

# Create your models here.s
from django.urls import reverse


class article(models.Model):
    Title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    body = models.TextField(editable=True, max_length=None)
    date = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True)

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})
