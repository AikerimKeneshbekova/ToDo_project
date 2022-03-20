from django.shortcuts import render, HttpResponse, redirect

from .models import Habits, ToDo

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def habits(request):
    habits_list = Habits.objects.all()
    return render(request, "habits.html", {"habits_list": habits_list}) 


def add_habits(request):
    form = request.POST
    text = form["habits_text"]
    habits1 = Habits(name = text)
    habits1.save()
    return redirect(habits) 

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text =text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def delete_habits(request, id):
    habits1 = Habits.objects.get(id=id)
    habits1.delete()
    return redirect(habits)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = True
    todo.save()
    return redirect(test)

def mark_habits(request, id):
    habits1 = Habits.objects.get(id=id)
    habits1.done_for_today = True
    habits1.save()
    return redirect(habits)

def unmark_habits(request, id):
    habits1 = Habits.objects.get(id=id)
    habits1.important = True
    habits1.save()
    return redirect(habits)

