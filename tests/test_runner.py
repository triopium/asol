import pytest

from asol.runner import Runner


@pytest.fixture
def validate():
    return Runner()


# def test_fail(validate):
# print("makak")
# assert validate.run() == "hello_bad"

# def test_nofail(validate):
# assert validate.run() == "hello"
