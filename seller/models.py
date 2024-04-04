from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_image = models.ImageField(upload_to='./main/static/img/products', default=None)
    item_name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=100, default=None)
    item_price = models.IntegerField()
    item_quantity = models.IntegerField()

    def __str__(self):
        return self.item_name


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=200)
    user_info = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    item_info = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart_item_quantity = models.IntegerField(default=1)
    cart_is_checkedout = models.BooleanField(default=False)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    cart_info = models.ForeignKey(Cart, on_delete=models.CASCADE)
    transaction_total_price = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
