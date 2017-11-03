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
                return "Oopsie! Time is up! I hope you finished this event!"
            hours=b.seconds//3600
            if(hours<0):
                hours=0
            minutes=(b.seconds//60)%60
            if(minutes<0):
                minutes=0
        
            return "You have "+str(b.days)+" days "+str(b.seconds//3600)+" hours "+str((b.seconds//60)%60)+" minutes remaining! Hurry up!!"

    def __str__(self):
        return self.eventname

    
    
