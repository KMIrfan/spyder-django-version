from django.urls import path
from .import views
app_name = 'customer'
urlpatterns = [
  
    path('', views.customer_index, name='index'),
    path('productdetails', views.customer_product, name='productdetails'),
    path('changepassword', views.customer_changepassword, name='changepassword'),
    path('profile', views.customer_profile, name='profile'),
    path('mycart', views.customer_mycart, name='mycart'),
    path('myorder', views.customer_myorder, name='myorder'),
]