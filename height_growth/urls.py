from django.urls import path
from height_growth.views import diet_plan_view

urlpatterns = [
    path('height-growth/', diet_plan_view, name='height_growth'),
]
