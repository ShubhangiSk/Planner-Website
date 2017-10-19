from django.shortcuts import render
from .models import Event
# Create your views here.
def login_page(request):
    events=Event.objects.all()
    return render(request, 'planner/login_page.html', {'events':events})
