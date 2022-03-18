from django.db import models


class ToMeet(models.Model):
    persone = models.CharField(max_length=40)
    phone_namber =models.CharField(max_length=16)
    date_of_meeting = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Goal_for_month(models.Model):
    goal = models.CharField(max_length=40)
    month = models.DateField(auto_now_add=False)
    difficulty = models.BooleanField(default=False)
    reason_for_goal= models.CharField(max_length=100)
    

    
