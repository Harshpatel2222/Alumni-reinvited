from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_view, name='home_view'),
    path('profile/',views.profile_view, name='profile'),
    path('base/',views.base_view, name='base'),
   
    
]