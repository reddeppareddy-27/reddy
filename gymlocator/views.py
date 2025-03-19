from django.shortcuts import render
from .models import State,District,City
from django.http import JsonResponse


def home1(request):
    states = State.objects.all()
    return render(request, 'gymlocator/index1.html', {'states': states})

def get_districts(request):
    state_id = request.GET.get('state_id')
    districts = list(State.objects.get(id=state_id).districts.values('id', 'name'))
    return JsonResponse({'districts': districts})

def get_cities(request):
    district_id = request.GET.get('district_id')
    cities = list(District.objects.get(id=district_id).cities.values('id', 'name'))
    return JsonResponse({'cities': cities})

def get_gyms(request):
    city_id = request.GET.get('city_id')
    gyms = list(City.objects.get(id=city_id).gyms.values('name', 'phone_number', 'google_maps_link'))
    return JsonResponse({'gyms': gyms})
