from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    username=models.ForeignKey('auth.User')
    eventname=models.CharField(max_length=500)
    description=models.TextField()
    created_date=models.DateTimeField(blank=True,null=True)
    starting_date=models.DateTimeField(default=timezone.now)
    deadline_date=models.DateTimeField(blank=True,null=True)

    def create(self):
        self.created_date=timezone.now()
        self.save()

    def add_deadline(self,deadline):
        self.deadline_date=deadline
        self.save()

    def __str__(self):
        return self.eventname

    
    
