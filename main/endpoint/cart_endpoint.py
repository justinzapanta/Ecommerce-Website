from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from seller.models import Cart, Item
from django.contrib.auth.models import User
import json

@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = Item.objects.get(item_id=data.get('id'))

        user = User.objects.get(username=request.session['user_email'])
        cart = Cart.objects.filter(item_info=item)


        if not cart:
            cart = Cart(item_info=item, user_info=user)
            cart.save()
            print('added to cart')
            return JsonResponse({'message' : 'success'}, status=201)
        else:
            print('already added')
            return JsonResponse({'message' : 'aleady added'}, status=201)
    return JsonResponse({'message', 'Failed'}, status=404)


