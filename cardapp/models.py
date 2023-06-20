from django.db import models

from django.contrib.auth.models import User
from ecom.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_item = models.IntegerField(default=0)
    isOrderd = models.BooleanField(default=False)
    quentity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username) + " " + str(self.product.product_name)


#create signal for total item fetch and all iten price add

@receiver(pre_save, sender=CartItem)
def my_handler(sender, **kwargs):
    cart_item = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_item.product.id)
    cart_item.price = cart_item.quentity * float(price_of_product.price)
    # total_cart_item = CartItem.objects.filter(user = cart_item.user)
    # cart_item.total_item = len(total_cart_item)

    # cart = Cart.objects.get(id=cart_item.cart.id)
    # cart.total_price = cart_item.price
    # cart.save()
 


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, blank=True)
    payment_id = models.CharField(max_length=100, blank=True)
    payment_signature = models.CharField(max_length=100, blank=True)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)  


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)      
    address = models.CharField(max_length=120)      
    locality = models.CharField(max_length=120)      
    landmark = models.CharField(max_length=120)      
    contact_number = models.CharField(max_length=11)      