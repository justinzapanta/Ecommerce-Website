from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_quantity = models.ImageField()


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=200)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart_quantity = models.IntegerField()
    cart_is_checkedout = models.BooleanField()
