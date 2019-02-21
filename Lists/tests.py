from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from Lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_handles_post_requests(self):
        response = self.client.post('/', {'item_text': 'a list item'})
        self.assertIn('a list item', response.content.decode())
        
