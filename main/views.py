from django.shortcuts import render

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
        'login' : False
    }

    if 'user_email' in request.session:
        data['login'] = True

    return render(request, 'main/shop/products.html', data)