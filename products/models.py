from django.db import models
from django.utils.text import slugify


class Allproducts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to="allproducts/")

    def __str__(self):
        return self.title


class Meat(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to="meat/")

    def __str__(self):
        return self.title


class Fruits(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to="fruite/")

    def __str__(self):
        return self.title


class Breads(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to="bread/")

    def __str__(self):
        return self.title


class Freeproducts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to="freeproducts/")

    def __str__(self):
        return self.title


class Organicvegetables(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to="organicvegetables/")

    def __str__(self):
        return self.title




