from django.urls import path
from .import views
app_name = 'customer'
urlpatterns = [
  
    path('', views.customer_index, name='index'),
    path('productdetails/<int:pid>', views.customer_product, name='productdetails'),
    path('changepassword', views.customer_changepassword, name='changepassword'),
    path('profile', views.customer_profile, name='profile'),
    path('mycart', views.customer_mycart, name='mycart'),
    path('myorder', views.customer_myorder, name='myorder'),
    path('update', views.customer_update, name='update'),
    path('get_total', views.get_total, name='get_total'),
    path('remove_cart/<int:cid>', views.remove_cart, name='remove_cart'),
    path('logout', views.logout, name='logout'),
    path('buy<int:pid>', views.buy, name='buy'),
    path('masterpage', views.masterpage, name='masterpage'),
   
    
]
