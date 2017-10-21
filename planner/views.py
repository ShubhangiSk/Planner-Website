from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .models import Event
from .forms import SignUpForm
# Create your views here.
def login_page(request):
    events=Event.objects.all()
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
    
