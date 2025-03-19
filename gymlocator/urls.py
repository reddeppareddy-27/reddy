from django.urls import path
from . import views

urlpatterns = [
    path('re/', views.home1, name='home1'),
    path('get-districts/', views.get_districts, name='get_districts'),
    path('get-cities/', views.get_cities, name='get_cities'),
    path('get-gyms/', views.get_gyms, name='get_gyms'),
]
