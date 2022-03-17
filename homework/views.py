from django.shortcuts import render, HttpResponse
from .models import ToMeet, Goal_for_month

def home(request):
    return render(request, "home.html")

def helloworld(request):
    return HttpResponse("добро пожаловать в приложение ToDo - Admin)")
 
def meeting(request):
    Tomeet_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"Tomeet_list": Tomeet_list})

def newHW(request):
    Goal_list = Goal_for_month.objects.all()
    return render(request, "newHW.html",{"Goal_list": Goal_list })