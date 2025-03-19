from django.urls import path
from services.views import *

urlpatterns=[
    path('services/',services,name="services"),
]