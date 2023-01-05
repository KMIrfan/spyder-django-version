from django.urls import path
from .import views
app_name = 'customer'
urlpatterns = [
  
    path('', views.customer_index, name='index'),
    path('productdetails', views.customer_product, name='productdetails'),
]