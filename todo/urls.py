"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from main.views import  test, homepage, habits, add_habits, add_todo, delete_todo, delete_habits
from homework.views import home, helloworld, meeting, newHW, add_tomeet, add_new, delete_tomeet,delete_goal
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage, name="home"),
    path("test/", test, name="test"),
    path("home", home, name="home"),
    path("",helloworld, name ="world"),
    path("meeting", meeting, name = "meeting"),
    path("newHW", newHW, name= "new"),
    path("add-tomeet/", add_tomeet, name ="add-tomeet"),
    path("habits", habits, name ="habits"),
    path("add_habits", add_habits, name= "add_habits" ),
    path("add_new", add_new, name="add_new"),
    path("add-todo/", add_todo, name = "add-todo"),
    path("delete-todo/<id>/", delete_todo, name = "delete-todo"),
    path("delete-tomeet/<id>/", delete_tomeet, name = "delete-tomeet"),
    path("delete-goal/<id>/", delete_goal, name= "delete-goal"),
    path("delete-habits/<id>", delete_habits, name="delete-habits")
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, Document_root=settings.MEDIA_ROOT) \
    
