from django.test import TestCase
from .models import Item


class TestView(TestCase):

    def test_get_todo_list(self):
        print('Testing the to do list home page is rendered')
        # Testing the response of the home page
        response = self.client.get('/')
        # Using the response codes to check the status of the page
        self.assertEqual(response.status_code, 200)
        # Checking the page template that was used to render the page
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        print('Testing the to do list add item page is rendered')
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        print('Testing the to do list edit item page is rendered')
        response = self.client.get(f'/edit/{item.id} ')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        print('Testing the Add Item page ')
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        print('Testing the delete item feature')
        response = self.client.get(f'/delete/{item.id} ')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        print('Testing the toggle item feature')
        response = self.client.get(f'/toggle/{item.id} ')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
