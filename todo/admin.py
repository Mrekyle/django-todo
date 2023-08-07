from django.contrib import admin


# Register your models here.

# once an item has been created inside the models File
# we need to import that into the admin file to allow it to be seen on the admin panel

from .models import Item