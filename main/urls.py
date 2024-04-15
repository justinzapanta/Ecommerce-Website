from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .backend import cart_backend, profile_backend, transaction_backend

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('signin/', include('user_authentication.urls')),
    path('seller/', include('seller.urls')),

    path('profile/', views.profile, name='profile'),

    #Cart End Point
    path('api/cart/add-item/', cart_backend.add_item),
    path('api/cart/delete-item/', cart_backend.delete_item),
    path('api/cart/update-quantity/', cart_backend.update_quantity),
    path('api/cart/place-order/', cart_backend.place_order),

    #Transaction End Point
    path('api/transaction/new-transaction/', transaction_backend.new_transaction, name='new transaction'),
    path('api/transaction/get-item', transaction_backend.get_item),

    #Profile End Point
    path('api/profile/update', profile_backend.change_personal_info),
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)