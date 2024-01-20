from django.test import TestCase
from app.serializers import *


class TestSerializer(TestCase):


    def test_category_serializer(self):
        category_serializer = CategorySerializer(data={
            "name":"first"
        })
        self.assertEqual(category_serializer.is_valid(), True)


    def test_category_name_required(self):
        category_serializer = CategorySerializer(data={
        })
        self.assertEqual(category_serializer.is_valid(), False)


    def test_category_name_unique(self):
        Category.objects.create(name="first")
        category_serializer = CategorySerializer(data={
             "name":"first"
        })
        self.assertEqual(category_serializer.is_valid(), False)

        
    def test_product_serializer_required_fields(self):
        cat = Category.objects.create(name="First")
        prod = {
             "name":"first",        
             "price":12,
             "qty": 1,
             "off": 12,
             "category":cat.id
        }


        # Without name test
        prod_without_name = prod.copy()
        prod_without_name.pop("name")
        prod_serializer_without_name = CreateProductSerializer(data=prod_without_name)
        self.assertEqual(prod_serializer_without_name.is_valid(), False)
       
        # Without price test
        prod_without_name = prod.copy()
        prod_without_name.pop("price")
        prod_serializer_without_name = CreateProductSerializer(data=prod_without_name)
        self.assertEqual(prod_serializer_without_name.is_valid(), False)

        # Without qty test
        prod_without_name = prod.copy()
        prod_without_name.pop("qty")
        prod_serializer_without_name = CreateProductSerializer(data=prod_without_name)
        self.assertEqual(prod_serializer_without_name.is_valid(), False)

      
        # Without off test
        prod_without_name = prod.copy()
        prod_without_name.pop("off")
        prod_serializer_without_name = CreateProductSerializer(data=prod_without_name)
        self.assertEqual(prod_serializer_without_name.is_valid(), False)

        # Without categroy test
        prod_without_name = prod.copy()
        prod_without_name.pop("category")
        prod_serializer_without_name = CreateProductSerializer(data=prod_without_name)
        self.assertEqual(prod_serializer_without_name.is_valid(), False)
    
   