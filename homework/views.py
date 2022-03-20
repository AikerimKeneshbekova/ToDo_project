from django.shortcuts import render, HttpResponse, redirect
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

def add_tomeet(request):
    form = request.POST
    text = form['Tomeet_text']
    Tomeet = ToMeet(persone = text)
    Tomeet.save()
    return redirect(meeting)

def add_new(request):
    form = request.POST
    text = form['new_text']
    new = Goal_for_month(goal = text)
    new.save()
    return redirect(newHW)

def delete_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(meeting)

def delete_goal(request, id):
    goal = Goal_for_month.objects.get(id=id)
    goal.delete()
    return redirect(newHW)

def mark_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = True
    tomeet.save()
    return redirect(meeting)


def unmark_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = False
    tomeet.save()
    return redirect(meeting)

def mark_goal(request, id):
    goal = Goal_for_month.objects.get(id=id)
    goal.difficulty = True
    goal.save()
    return redirect(newHW)

def unmark_goal(request, id):
    goal = Goal_for_month.objects.get(id=id)
    goal.difficulty = False
    goal.save()
    return redirect(newHW)


