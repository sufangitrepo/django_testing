from django.test import TestCase
from app.models import *

class ModelTest(TestCase):


    def setUp(self) -> None:
        # self.category = Category.objects.create(name="first") 
        return super().setUp()
    
    def test_category_name_unique(self):
        category1 = Category.objects.create(name="first") 
       



