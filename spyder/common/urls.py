from django.urls import path
from .import views
app_name = 'common'
urlpatterns = [
  
    path('', views.common_index, name='index'),
    path('login', views.common_login, name='login'),
    path('sellerlogin', views.common_sellerlogin, name='sellerlogin'),
    path('customersignup', views.common_customersignup, name='customersignup'),
    path('sellersignup', views.common_sellersignup, name='sellersignup'),

]
