from django.db import models


class Shopvegetable(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    newprice = models.IntegerField(default=0)
    oldprice = models.IntegerField(default=0)
    img = models.ImageField(upload_to='shop/')

    def __str__(self):
        return self.name


