from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "home.html")

def helloworld(request):
    return HttpResponse("добро пожаловать в приложение ToDo - Admin)")
