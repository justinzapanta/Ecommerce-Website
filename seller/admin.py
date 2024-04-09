from django.contrib import admin
from .models import Item, Cart, Transaction
# Register your models here.

admin.site.register([
    Item,
    Cart,
    Transaction
])
