from django.urls import path
from . import views

urlpatterns =[
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/update/', views.update_profile, name='update_profile'),

]