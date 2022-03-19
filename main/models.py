from django.db import models

class Habits(models.Model):
    name = models.CharField(max_length=40)
    done_for_today = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    comment = models.TextField()
