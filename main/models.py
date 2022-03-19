from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed =models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Habits(models.Model):
    name = models.CharField(max_length=40)
    done_for_today = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    comment = models.TextField()
