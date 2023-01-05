from django.urls import path
from .import views
app_name = 'spyderadmin'
urlpatterns = [
  
    path('', views.spideradmin_index, name='index'),
    path('approveseller', views.spideradmin_approveseller, name='approveseller'),
    path('viewseller', views.spideradmin_viewseller, name='viewseller'),
    path('viewcustomer', views.spideradmin_viewcustomer, name='viewcustomer'),

    

]