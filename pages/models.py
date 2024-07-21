from django.db import models
from home.admin import Users


class Cardpage(models.Model):
    img = models.ImageField(upload_to="cards/")
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    handle = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Cards(models.Model):
    subtotal = models.IntegerField()
    total_price = models.IntegerField()
    total = models.IntegerField()
    shipping = models.BooleanField(default=False)
    cardnumber = models.CharField(max_length=16)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)


