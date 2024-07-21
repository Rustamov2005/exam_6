from django.db import models


class Maxsulot(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField()
    description = models.TextField()
    count = models.IntegerField()
    img = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name


class Related(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='imgs/')
    price = models.IntegerField()

    def __str__(self):
        return self.name






