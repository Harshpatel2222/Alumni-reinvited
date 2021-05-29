from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_view, name='home_view'),  
    path('profile/',views.profile_view, name='profile_view'),
    path('connections/',views.connections_view, name='connections_view'),
    path('events/',views.events_view, name='events_view'),
    path('jobs/',views.jobs_view, name='jobs_view'),
    path('team/',views.team_view, name='team_view'),
    path('contact/',views.contact_view, name='contact_view'),
    path('signin/',views.sign_view, name='sign_view'),
]