from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Event(models.Model):
    username=models.ForeignKey('auth.User')
    eventname=models.CharField(max_length=500)
    description=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    starting_date=models.DateTimeField(default=timezone.now)
    deadline_date=models.DateTimeField()
    category_choices=(('official_event','Official Event'),('personal_event','Personal Event'),('fun_event','Fun Event'))
    priority_choices=((1, 'High Priority'),(2,'Medium Priority'),(3,'Low Priority'))
    category=models.CharField(max_length=20,choices=category_choices, default='personal_event')
    priority=models.IntegerField(choices=priority_choices,default=1)
    event_completed=models.BooleanField(default=False)

    def create(self):
        self.created_date=timezone.now()
        self.save()

    def add_deadline(self,deadline):
        self.deadline_date=deadline
        self.save()

    def get_remaining_days(self):
        if self.deadline_date:
            dd=self.deadline_date
            a=datetime.datetime.now(datetime.timezone.utc)
            b=dd-a
            days=b.days
            if(days<0):
                self.event_completed=True
                self.save()
                return "Oopsie! Time is up! I hope you finished this event!"
            self.event_completed=False
            self.save()
            hours=b.seconds//3600
            if(hours<0):
                hours=0
            minutes=(b.seconds//60)%60
            if(minutes<0):
                minutes=0
        
            return "You have "+str(b.days)+" days "+str(b.seconds//3600)+" hours "+str((b.seconds//60)%60)+" minutes remaining."


    def get_category(self):
        if self.category=="official_event":
            return "This is an Official event"
        elif self.category=="personal_event":
            return "This is a personal event"
        else:
            return "Yayy! This is a fun event"

    def get_priority(self):
        if self.priority==1:
            return "HIGH priority"
        elif self.priority==2:
            return "MEDIUM priority"
        else:
            return "LOW priority"

    def get_color(self):
        if self.priority==1:
            return "red"
        elif self.priority==2:
            return "blue"
        elif self.category=="fun_event":
            return "hotpink"
        else:
            return "green"
    
    def __str__(self):
        return self.eventname

    
    
