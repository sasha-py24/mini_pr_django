from django.db import models

from shop.models import Product
from core.models import TimeStampedMixin


class Order(TimeStampedMixin):
    name = models.ForeignKey('shop.Product', on_delete=models.SET_NULL, null=True,blank=True )
    products = models.ManyToManyField('shop.Product', related_name='orders', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)