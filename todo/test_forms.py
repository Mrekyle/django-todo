# Default testing framework with the django framework
from django.test import TestCase
# Importing the form class from the forms file
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        print('Testing is item name is required')
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_required(self):
        print('Testing if field is required')
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_forms_meta_class(self):
        print('Testing is item fields have changed')
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])


"""
You can test individual test files by adding on the file name into the test
command such as

python3 manage.py test todo.test_forms
"""
