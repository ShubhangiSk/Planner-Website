from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event

class CustomAdminSplitDateTime(widgets.AdminSplitDateTime):
    def __init__(self, attrs=None):
        widgets1 = [widgets.AdminDateWidget, widgets.AdminTimeWidget(attrs=None, format='%I:%M %p')]
        forms.MultiWidget.__init__(self, widgets1, attrs)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class EventForm(forms.ModelForm):

    class Meta:
        model=Event
        widgets = {
            'eventname' : forms.TextInput(attrs={'class': 'input-mini'}),
            'description' : forms.TextInput(attrs={'class': 'input-mini'}),
            'deadline_date':forms.DateTimeInput(attrs={'type': 'date'})
        }
        fields=('eventname','description','deadline_date','category','priority')
        
