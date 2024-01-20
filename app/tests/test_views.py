from django.test import TestCase, Client
from app.models import *


class AppViewTest(TestCase):

    def setUp(self) -> None:
        self.category_url = '/app/api/category/'
        self.category = Category.objects.create(name='first')
        self.category2 = Category.objects.create(name='second')
        return super().setUp()
    
    def test_app_product_post(self): 
        product_url = '/app/api/product'
       
        list_of_products = [
            {
                "name":"product",
                "price":12,
                "qty": 12,
                "category": self.category.id,
                "off": 12
           },
            {
                "name":"product1",
                "price":12,
                "qty": 12,
                "category": self.category.id,
                "off": 12
           }
        ] 
        for prod in list_of_products:
            response = self.client.post(product_url,prod, content_type='application/json')
            self.assertEqual(response.status_code, 200)
        
    def test_app_product_post_with_same_name_with_same_cateogry(self): 
        product_url = '/app/api/product'
        list_of_products = [
            {
                "name":"product",
                "price":12,
                "qty": 12,
                "category": self.category.id,
                "off": 12
           },
            {
                "name":"product",
                "price":12,
                "qty": 12,
                "category": self.category.id,
                "off": 12
           }
        ] 
    
        response = self.client.post(product_url,list_of_products[0], content_type='application/json')
        response = self.client.post(product_url,list_of_products[1], content_type='application/json')
        self.assertEqual(response.status_code, 400)
            
    def test_app_product_post_with_same_name_but_different_cateogry(self): 
        product_url = '/app/api/product'
        # category1 = Category.objects.create(name='first')
        # category2 = Category.objects.create(name='second')
        list_of_products = [
            {
                "name":"product",
                "price":12,
                "qty": 12,
                "category": self.category.id,
                "off": 12
           },
            {
                "name":"product",
                "price":12,
                "qty": 12,
                "category": self.category2.id,
                "off": 12
           }
        ] 
        for prod in list_of_products:
            response = self.client.post(product_url,prod, content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_app_category_post(self):
        list_of_category = [
            {"name":"fruits",
             },
             {"name":"vegitables",
             },
        ]
        for categoy in list_of_category:
            response = self.client.post(self.category_url,categoy,"application/json")
            self.assertEqual(response.status_code, 201)

    def test_app_category_with_same_name_post(self):
        list_of_category = [
            {"name":"fruits",
             },
             {"name":"fruits",
             },
        ]
        response = self.client.post(self.category_url,list_of_category[0],"application/json")
        response = self.client.post(self.category_url,list_of_category[1],"application/json")
        self.assertEqual(response.status_code, 400)

    def test_app_category_delete(self):
        
        response = self.client.delete(self.category_url + str(self.category.id)+"/","application/json")
        self.assertEqual(response.status_code, 204)

    def test_app_category_get(self):
        response = self.client.get(self.category_url,)
        self.assertEqual(response.status_code, 200)

    def test_app_category_detail_get(self):
        response = self.client.get(self.category_url+str(1)+'/')
        self.assertEqual(response.status_code, 200)
    
    def test_app_category_patch(self):
        
        response = self.client.patch(self.category_url+str(self.category.id)+'/',{"name":"changed"}, "application/json")
        cate = Category.objects.all().first() 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(cate.name, "changed")

