"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list

    # """
    # The url patterns is the same as the app.route in flask. Using the path 
    # method we specify the url, the name of the function/page and then the 
    # name that we call it. 
    # """
urlpatterns = [
    path('admin/', admin.site.urls),
    # leaving an empty string means we will hit the default home page of the application
    # without specifying what page to go to
    path('', get_todo_list, name='To Do List Application'),
]
