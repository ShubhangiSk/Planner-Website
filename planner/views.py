from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Event
from .forms import SignUpForm
from .forms import EventForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'planner/event_detail.html', {'event': event})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.username = request.user
            event.starting_date =timezone.now()
            event.save()
            return redirect('login_page')
    else:
        form = EventForm()
    return render(request, 'planner/add_new_event.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.username = request.user
            event.created_date = timezone.now()
            
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'planner/add_new_event.html', {'form': form})

def login_page(request):
    if request.user.is_anonymous():
        events=Event.objects.filter(eventname__contains="Python")
    else:  
        events=Event.objects.filter(username=request.user)
    return render(request, 'planner/login_page.html', {'events':events})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login_page')
    else:
        form = SignUpForm()
    return render(request, 'planner/sign_up.html', {'form': form})
    
