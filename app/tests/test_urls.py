from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *


class AppUrlTest(SimpleTestCase):
    
    def test_app_url_product_resolve(self):
        url = reverse('product')
        resolve_match = resolve(url)
        self.assertEqual(resolve_match.func.view_class, ProductView)

    
    def test_app_url_category_resolve(self):
        category_url = reverse('category-list', args=[])
        resolve_match = resolve(category_url)
        self.assertEqual(resolve_match.func.__name__, CategoryView.__name__)
    
    
    
