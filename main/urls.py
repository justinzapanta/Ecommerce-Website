from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('signin/', include('user_authentication.urls')),
]