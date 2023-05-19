from django.db import models
from store.models import Product
# Create your models here.

class Cart(models.Model):
    cart_id   = models.CharField(max_length= 50, blank= True)
    date_joined = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.cart_id


class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE),
    cart    = models.ForeignKey(Cart, on_delete= models.CASCADE),
    quantity = models.IntegerField()
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return self.product

