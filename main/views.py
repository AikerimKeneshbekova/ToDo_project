from django.shortcuts import render, HttpResponse

from .models import Habits

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")


def habits(request):
    habits_list = Habits.objects.all()
    return render(request, "habits.html", {"habits_list": habits_list}) 

