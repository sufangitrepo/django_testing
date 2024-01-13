import pytest

@pytest.mark.skip
def test_1():
    print("BC")
    assert 1 == 1

@pytest.mark.skip
def test_2():
    print("BC")
    assert 1 == 1


# fixtures

@pytest.fixture(scope="session")
def fetch_data_from_db():
    print("this is fixture")
    return "hello"


def test_with_fixture(fetch_data_from_db):
    assert fetch_data_from_db == "hello"

def test_without_fixture(fetch_data_from_db):
    assert fetch_data_from_db == "hello"
    
