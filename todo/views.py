from django.shortcuts import render

# Create your views here.

# This is where the views/webpage information for the end user goes into 

# def say_hello(request):
#     return HttpResponse("Hello")
def get_todo_list(request):
    """
    using the render method we can return the templates html File
    to the end user of the application 

    In return this will render any html code that is written inside of that file
    """
    return render(request, 'todo/todo_list.html')