from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from Lists.views import home_page
from Lists.models import Item

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_handles_post_requests(self):
        response = self.client.post('/', {'item_text': 'a list item'})
        self.assertIn('a list item', response.content.decode())
        

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list.item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list.item')
        self.assertEqual(second_saved_item.text, 'Item the second')
