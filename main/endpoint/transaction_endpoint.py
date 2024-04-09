from django.contrib.auth.models import User
from seller.models import Item, Cart, Transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

def total_price(cart):
    price = 0

    for item in cart:
        price = price + item.cart_item_total_price

    return price    
    

def new_transaction(request):
    if 'user_email' in request.session:
        user = User.objects.get(username=request.session['user_email'])
        transaction = Transaction.objects.filter()
        cart = Cart.objects.filter(user_info=user)

        number = 1
        price = total_price(cart)

        if transaction:
            number = transaction[-1].transaction_invoice

        for item in cart:
            item.cart_is_checkedout = True
            transaction = Transaction(
                cart_info=item,
                transaction_invoice=number,
                transaction_total_price=price)
            item.save()
            transaction.save()

        return redirect('shop')
    return redirect('sign_in')