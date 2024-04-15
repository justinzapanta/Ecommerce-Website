from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

@csrf_exempt
def change_personal_info(request):
    if 'user_email' in request.session and request.method == 'POST':
        data = json.loads(request.body)

        user = User.objects.get(username=request.session['user_email'])
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.username = data['email']
        user.save()
        
        request.session['user_email'] = user.username
        
        return JsonResponse({'message' : 'success'}, status=200)
    return JsonResponse({'message' : 'login'}, status=400)


    