import pytest
from django.contrib.auth.models import User



@pytest.fixture()
def create_user_fixture_factory(db):
    
    def create_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return create_user


@pytest.fixture()
def create_user_fixture(create_user_fixture_factory):
    user = create_user_fixture_factory(username="ali", email="ali@gmail.com")
    return user

@pytest.fixture()
def create_staff_user_fixture(create_user_fixture_factory):
    user = create_user_fixture_factory(username="ali", email="ali@gmail.com", is_staff=True)
    return user

from tests.factories import UserFactory, ProductFactory, CategoryFactory
from pytest_factoryboy import register


register(UserFactory)  #user_factory
register(CategoryFactory)  #category_factory
register(ProductFactory)  #product_factory


@pytest.fixture(scope="function")
def create_user_fixture(db, user_factory):
    return user_factory.create()


@pytest.fixture(scope="function")
def create_product_fixture(db, product_factory):
    return product_factory.create()

@pytest.fixture(scope="function")
def create_category_fixture(db, category_factory):
    return category_factory.create_batch(3)