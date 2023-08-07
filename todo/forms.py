from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """
    The inner class tells the parent class information about itself.
    What it should display/do/how to do things.

    This class is essentially telling the application to build a form with the
    paramaters defined below. Allowing us to delete the html form in the
    add_item.html file
    """
    class Meta:
        model = Item
        fields = ['name', 'done']
