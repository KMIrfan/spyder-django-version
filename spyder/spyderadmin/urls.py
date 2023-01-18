from django.urls import path
from .import views
app_name = 'spyderadmin'
urlpatterns = [
  
    path('index', views.spideradmin_index, name='index'),
    path('approveseller', views.spideradmin_approveseller, name='approveseller'),
    path('viewseller', views.spideradmin_viewseller, name='viewseller'),
    path('viewcustomer', views.spideradmin_viewcustomer, name='viewcustomer'),
    path('', views.spideradmin_login, name='login'),
    path('viewproducts', views.viewproducts, name='viewproducts'),
    path('logout', views.logout, name='logout'),
    path('removecustomer', views.removecustomer, name='removecustomer'),
    path('removecust', views.removecust, name='removecust'),
    path('removeproduct', views.removeproduct, name='removeproduct'),
    path('removepro', views.removepro, name='removepro'),
    path('removeseller', views.removeseller, name='removeseller'),
    path('removesell', views.removesell, name='removesell'),
    path('approveseller/<int:sid>', views.approveseller, name='approveseller'),
    path('rejectseller/<int:sid>', views.rejectseller, name='rejectseller'),
    path('masterpage', views.masterpage, name='masterpage'),


    

]