from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .endpoint import cart_endpoint, transaction_endpoint, profile_endpoint

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('signin/', include('user_authentication.urls')),
    path('seller/', include('seller.urls')),

    path('profile/', views.profile, name='profile'),

    #Cart End Point
    path('api/cart/add-item/', cart_endpoint.add_item),
    path('api/cart/delete-item/', cart_endpoint.delete_item),
    path('api/cart/update-quantity/', cart_endpoint.update_quantity),
    path('api/cart/place-order/', cart_endpoint.place_order),

    #Transaction End Point
    path('api/transaction/new-transaction/', transaction_endpoint.new_transaction, name='new transaction'),
    path('api/transaction/get-item', transaction_endpoint.get_item),

    #Profile End Point
    path('api/profile/update', profile_endpoint.change_personal_info),
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)