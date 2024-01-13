import pytest
from django.contrib.auth.models import User


# def test_check_created_staff_user(create_user_fixture):
#     # user = user_factory.build()
#     # user.save()
#     print(User.objects.count())
#     assert create_user_fixture.is_staff 

# def test_product_created(db, product_factory):
#     prod = product_factory.create()
#     assert prod is not None

def test_create_product(create_product_fixture):
    print(create_product_fixture)
    assert create_product_fixture is not None

def test_create_category(create_category_fixture):
    print(create_category_fixture)
    assert create_category_fixture is not None

