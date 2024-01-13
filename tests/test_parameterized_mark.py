import pytest
from app.models import *

@pytest.mark.parametrize(
    "name, category, price, validity",
    [
        ("first", 1, 12, True),
        ("second", 1, 122, True),
    ]
)
def test_create_product(db, product_factory, name, category, price, validity):
    product_factory(name=name,category_id=category,price=price)
    items = Product.objects.all().count()
    assert items == validity


@pytest.mark.parametrize(
        "name, validity",
        [
            ("Fruit", True, ),
            ("Banana", True, )
        ]
)
def test_create_category_instance(db, category_factory, name, validity):
    category_factory(name=name)
    items = Category.objects.all().count()
    assert items == validity 

"""
  Api testing calling api
"""
@pytest.mark.parametrize(
    "name, price, validity",
    [
        ("first",  12, 201),
        ("second",  122, 201),
    ],
)
@pytest.mark.django_db
def test_product_create_api(client, category_factory,  name, price, validity ):
       category = category_factory.create()
       response = client.post(
                "/product/",
                data={
                    "name":name,
                    "category":category.id,
                    "price":price
                }
            )
       assert response.status_code == validity