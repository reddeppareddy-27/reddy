from django.contrib import admin
from .models import State, District, City, Gym

# Register your models here
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Gym)
