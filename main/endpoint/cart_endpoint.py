from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from seller.models import Cart, Item
from django.contrib.auth.models import User
from django.shortcuts import redirect
import json

@csrf_exempt
def add_item(request):
    if 'user_email' in request.session:
        if request.method == 'POST':
            data = json.loads(request.body)
            item = Item.objects.get(item_id=data.get('id'))
            cart = Cart.objects.filter(item_info=item)
            user = User.objects.get(username=request.session['user_email'])


            if not Cart.objects.filter(item_info=item, user_info=user):
                cart = Cart(item_info=item, user_info=user)
                cart.save()
                return JsonResponse({'message' : 'success'}, status=201)
            else:
                return JsonResponse({'message' : 'aleady added'}, status=202)
    return JsonResponse({'message', 'Failed'}, status=203)



@csrf_exempt
def delete_item(request):
    if 'user_email' in request.session:
        if request.method == 'POST':
            data = json.loads(request.body)
            user = User.objects.get(email=request.session['user_email'])
            if not 'item_id' in data:
                print('run')
                cart = Cart.objects.get(cart_id=data.get('cart_id'), user_info=user)
                cart.delete()

            else:
                item = Item.objects.get(item_id=data.get('item_id'))
                cart = Cart.objects.get(item_info=item, user_info=user)
                cart.delete()

            return JsonResponse({'message' : 'Deleted'}, status=201)
        return JsonResponse({'message' : 'Failed'}, status=203)
    return JsonResponse({'message' : 'Please Login'}, status=203)



