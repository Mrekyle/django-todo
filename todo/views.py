from django.shortcuts import render, redirect
# Allowing the use of the item database inside of the views file.
# allowing us to render the database items
from .models import Item

# Create your views here.

# This is where the views/webpage information for the end user goes into

# def say_hello(request):
#     return HttpResponse("Hello")


def get_todo_list(request):
    """
    using the render method we can return the templates html File
    to the end user of the application 

    In return this will render any html code that is written inside of that 
    file
    """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """
    Adding another page is as simple as adding the href to the 
    page file/button and creating a new function to render that page

    Also not forgetting to add the page into the urls.py file
    """
    if request.method == 'POST':
        name = request.POST.get('item_name')  # Getting the items name
        done = 'item_done' in request.POST  # Getting the items boolean value of the checkbox
        # Passing the items variables to the create object method. To create it on the database
        Item.objects.create(name=name, done=done)

        print(request.POST)
        print('Done value: ', done)

        #  Using the redirect method it redirects the user to the 'home'/previous page. - Remembering redirect needs importing
        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html',)
