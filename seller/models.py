from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_image = models.ImageField(upload_to='product/images', default='Null')
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_quantity = models.IntegerField()

    def __str__(self):
        return self.item_name


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=200)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart_quantity = models.IntegerField()
    cart_is_checkedout = models.BooleanField()

    def __str__(self):
        return self.cart_id


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    transaction_total_price = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id