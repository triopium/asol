import os
import tempfile
import typing

import pytest

# from asol.params import *
# @pytest.fixture(scope="session")
# def test_tmp(tmpdir):
# print("ehllů")
# print("ehllů")
# temp_dir = tmpdir.mkdir("my_temp_dir")
# print(temp_dir)
# print("ehllů")
# def


@pytest.fixture(scope="session")
def temporary_directory(tmpdir_factory):
    # Create a temporary directory at the session level
    temp_dir = tmpdir_factory.mktemp("my_temp_dir")
    return temp_dir


def test_args(temporary_directory):
    print(temporary_directory)
    os.chdir(temporary_directory)
    print(os.getcwd())


# def test_pars():
