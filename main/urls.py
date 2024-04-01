from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('signin/', include('user_authentication.urls')),
    path('seller/', include('seller.urls'))
    
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)