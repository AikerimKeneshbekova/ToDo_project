from django.shortcuts import render, HttpResponse
from .models import ToMeet

def home(request):
    return render(request, "home.html")

def helloworld(request):
    return HttpResponse("добро пожаловать в приложение ToDo - Admin)")
 
def meeting(request):
    Tomeet_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"Tomeet_list": Tomeet_list})