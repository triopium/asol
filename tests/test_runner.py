import pytest, os
from asol.runner import *
import unittest
import logging
logerr = logging.getLogger(__name__)
import git
import tempfile

### simple
def test_debug_test():
    """deubug test"""
    # logerr.info("hello")
    assert debug_test() == True

### with unittest
class DebugTest(unittest.TestCase):
    def test_debug_test_true(self):
        """must pass"""
        self.assertTrue(debug_test())

### table driven
@pytest.fixture
def destination_path_cases():
    return [
        ("2020-01-01_1.json","2020/W1/01-01_1.json"),
        ("2021-01-01_1.json","2020/W53/01-01_1.json"),
        ("2021-02-10_1.json","2021/W6/02-10_1.json"),
    ]

def test_destination_path(destination_path_cases):
    for filename, expected in destination_path_cases:
        dt=date_from_filename(filename)
        sq,ok=extract_seqnum(filename)
        result = destination_path(dt,sq)
        assert expected == result

### test with temp directory
@pytest.fixture(scope="session")
def temp_dir(tmpdir_factory):
    # Create a temporary directory at the session level
    temp_dir = tmpdir_factory.mktemp("my_temp_dir")
    return temp_dir

def test_with_temp_dir(tmpdir):
    ### Clone assignmet
    logerr.info(tmpdir)
    url="https://github.com/czech-radio/assignment"
    repo_path = git.Repo.clone_from(url, tmpdir)
    logerr.info(repo_path)
    ### Run prepare.py inside assignment
    #### ensure that the script sees only the tmp dir

### test class
# @pytest.fixture
# def validate():
    # return Runner()

# def test_nofail(validate):
# assert validate.run() == "hello"

