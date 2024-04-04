from django.shortcuts import render
from .items import Items
from seller.models import Cart
from django.contrib.auth.models import User
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
    }

    if 'user_email' in request.session:
        data['login'] = True
        email = request.session['user_email']
        data['cart_items'] = Cart.objects.filter(user_info=User.objects.get(username=email))

    if request.method == 'POST':
        search = ''
        if 'search' in request.POST:
            search = request.POST['search']
        elif 'mobile-view-search' in request.POST:
            search = request.POST['mobile-view-search']

        data['items'] = items.search(search)
        data['types'] = items.get_type(search)
    
    data['items'] = items.for_column(data['items'], 1)
    return render(request, 'main/shop/products.html', data)
