from django.shortcuts import render

import sys
sys.path.insert(0, '..')

from seller.models import Item
# Create your views here.

def index(request):
    data = {
        'login' : False    
    }

    if 'user_email' in request.session:
        data['login'] = True

    return render(request, 'main/index.html', data)


def shop(request):
    data = {
        'login' : False,
        'items' : Item.objects.all()
    }

    if 'user_email' in request.session:
        data['login'] = True

    return render(request, 'main/shop/products.html', data)