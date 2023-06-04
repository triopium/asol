import pytest
from asol.parse import Runner

@pytest.fixture
def parser():
 return Runner()

def test_parsing(parser):
    assert parser.run() == "hello"
    # print("kex")
