from django.shortcuts import render
from .models import DietPlan

def diet_plan_view(request):
    diet_plans = DietPlan.objects.prefetch_related('exercises__animations').all()
    return render(request, 'height_growth/height.html', {
        'diet_plans': diet_plans,
    })