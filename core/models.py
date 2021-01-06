from django.conf import settings
from django.db import models

# Create your models here.

# Items that can be purchased


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def _str_(self):
        return self.title


# Will be where items specific to order are stored
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

# Will link all order items - shopping cart
# When logged in, should fetch shopping cart


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def _str_(self):
        return self.title
