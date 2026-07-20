from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('services/', views.services, name='services'),
    path('request_pickup/', views.request_pickup, name='request_pickup'),
    path('update_pickup/<int:pk>/', views.update_pickup, name='update_pickup'),
    path('delete_pickup/<int:pk>/', views.delete_pickup, name ='delete_pickup'),
    path('companies/', views.company_list, name='companies'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail')
    
  
    



    

]