import factory
from django.contrib.auth.models import User
from app.models import Category, Product
from django.utils import timezone 
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = True


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = fake.name()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = fake.name()
    category = factory.SubFactory(CategoryFactory)
    price = 12


 