from django.contrib.auth.models import User
from seller.models import Item, Cart, Transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

def total_price(cart):
    price = 0

    for item in cart:
        price = price + item.cart_item_total_price

    return price    


def decrease_item_quantity(cart):
    items = Item.objects.all()
    for cart_item in cart:
        for item in items:
            if cart_item.item_info.item_id == item.item_id:
                item.item_quantity = item.item_quantity - cart_item.cart_item_quantity
                item.save()


def new_transaction(request):
    if 'user_email' in request.session:
        user = User.objects.get(username=request.session['user_email'])
        transaction = Transaction.objects.filter()
        cart = Cart.objects.filter(user_info=user, cart_is_checkedout=False)

        number = 1
        price = total_price(cart)

        if len(transaction) >= 1:
            number = len(transaction) + 1
        else:
            number = 1
            
        for item in cart:
            item.cart_is_checkedout = True
            transaction = Transaction(
                cart_info=item,
                transaction_invoice=number,
                transaction_total_price=price,
                user_info=user
            )
            item.save()
            transaction.save()
        decrease_item_quantity(cart)

        return redirect('shop')
    return redirect('sign_in')


@csrf_exempt
def get_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        if 'invoice_number' in data:
            transactions = Transaction.objects.filter(transaction_invoice=data['invoice_number'])
            transaction_list = []

            for transaction in transactions:
                transaction_list.append([
                    transaction.cart_info.item_info.item_image.url,
                    transaction.cart_info.item_info.item_name,
                    transaction.cart_info.cart_item_quantity,
                    transaction.cart_info.cart_item_total_price,
                ])
            
        return JsonResponse({
                'item_list' : transaction_list,
                'length' : len(transaction_list)
            },status=200
        )