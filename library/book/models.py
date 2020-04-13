from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    amazon_url = models.URLField(max_length=200)
    author = models.CharField(max_length=30, default='anonymous')
    genre = models.CharField(max_length=200, default='N/a')

    def __str__(self):
        return self.title
