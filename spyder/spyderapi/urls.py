from django.urls import path
from .import views
app_name = 'spyderapi'
urlpatterns = [
  
    path('addstudent', views.add_student, name='index'),
    path('loadstudents', views.view_student, name='view'),
    path('deletestudent/<int:sid>', views.delete_student, name='delete'),
    path('updatestudent/<int:sid>', views.update_student, name='update')
    


]
