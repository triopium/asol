import os
import tempfile
import typing
import pytest

@pytest.fixture(scope="session")
def temporary_directory(tmpdir_factory):
    # Create a temporary directory at the session level
    temp_dir = tmpdir_factory.mktemp("my_temp_dir")
    return temp_dir

def test_args(temporary_directory):
    print(temporary_directory)
    os.chdir(temporary_directory)
    print(os.getcwd())
