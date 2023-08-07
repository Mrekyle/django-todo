from django.db import models

# Create your models here.

# This is where the database's are created in
# By using classes we create the databases and all that they contain

class Item(models.Model):
    """
    null and blank ensure that an item cant be created empty. 
    Meaning it has to have information inside of the fields
    We dont have to create an id field as Django does this for us.

    Once we have created the required class. Run the command
    python3 manage.py makemigrations --dry-run - To ensure everything looks correct
    then run it without the dry run parameter to execute the command. And 
    Django will create a file with the code to create that database in the migrations folder.
    """
    name = models.CharField(max_length=50 , null=False, blank=False)  # CharField means it will just have characters or text
    done = models.BooleanField(null=False, blank=False, default=False)  # True of false