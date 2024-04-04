from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .endpoint import cart_endpoint

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('signin/', include('user_authentication.urls')),
    path('seller/', include('seller.urls')),    

    #End Point
    path('api/cart/add-item/', cart_endpoint.add_item)
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)