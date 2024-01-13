import pytest
from django.contrib.auth.models import User

# @pytest.fixture(scope="function")
# def create_user_fixture(db):
#     return User.objects.create_user("abc")



# def test_created_user(create_user_fixture):
#     create_user_fixture.set_password("hello")
#     assert create_user_fixture.check_password("hello")


# def test_created_user2(create_user_fixture):
#     count = User.objects.count()
#     assert count == 1




def test_created_user(create_user_fixture):
    create_user_fixture.set_password("hello")
    assert create_user_fixture is not None


def test_created_super_user(create_staff_user_fixture):
    assert create_staff_user_fixture.is_staff