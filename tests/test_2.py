import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_add_user_in_db_test():
    user = User.objects.create_user("ali", "ali@gmail.com", "123")
    assert user.email == 'ali@gmail.com'
