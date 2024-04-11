from django.shortcuts import render, redirect
from .items import Items
from seller.models import Cart, Transaction
from django.contrib.auth.models import User
import json
# Create your views here.

def index(request):
    data = {'login' : False}

    if 'user_email' in request.session:
        data['login'] = True

    return render(request, 'main/index.html', data)

def shop(request):
    items = Items()
    data = {
        'login' : False,
        'items' : items.items,
        'types' : items.get_type(),
        'item_count' : 0
    }

    #check if the user is login
    if 'user_email' in request.session:
        data['login'] = True
        email = request.session['user_email']
        data['cart_items'] = Cart.objects.filter(user_info=User.objects.get(username=email), cart_is_checkedout=False)
        data['item_count'] = len(data['cart_items'])


    #for search
    if request.method == 'POST':
        search = ''
        if 'search' in request.POST:
            search = request.POST['search']
        elif 'mobile-view-search' in request.POST:
            search = request.POST['mobile-view-search']

        data['items'] = items.search(search)
        data['types'] = items.get_type(search)
    
    
    items = items.for_column(data['items'])
    data['items'] = items
    return render(request, 'main/shop/products.html', data)


def profile(request):
    if 'user_email' in request.session:
        user = User.objects.get(username=request.session['user_email'])
        transactions = Transaction.objects.filter(user_info=user)
        item_group = []
        filter_transaction = []
        temp_list = []

        reference = 'null'
        for index, transaction in enumerate(transactions):
            if reference == 'null' or reference == transaction.transaction_invoice:
                if reference == 'null':
                    filter_transaction.append(transaction)

            else:
                filter_transaction.append(transaction)

                if len(transactions) == (index+ 1 ):
                    item_group.append(temp_list)

            reference = transaction.transaction_invoice
        

        return render(request, 'main/profile/profile.html', {
            'user' : user,
            'transactions' : filter_transaction,
            'item_group' : item_group,

        })
    return redirect('sign_in')
