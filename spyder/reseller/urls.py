from django.urls import path
from .import views
app_name = 'reseller'
urlpatterns = [
  
    path('', views.reseller_index, name='index'),
    path('changepassword', views.reseller_changepassword, name='changepassword'),
    path('profile', views.reseller_profile, name='profile'),
    path('addproduct', views.reseller_addproduct, name='addproduct'),
    path('productcatelogue', views.reseller_productcatelogue, name='productcatelogue'),
    path('recentorders', views.reseller_recentorders, name='recentorders'),
    path('updatestock', views.reseller_updatestock, name='updatestock'),
    
]