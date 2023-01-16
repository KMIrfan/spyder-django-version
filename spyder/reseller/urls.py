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
    path('update', views.reseller_update, name='update'),
    path('stock_up', views.stock_up, name='stock_up'),
    path('add_stock', views.add_stock, name='add_stock'),
    path('logout', views.logout, name='logout'),
    
    
]