import pytest
import os


@pytest.fixture
def create_directories():
    newpath = r'C:\pytest'
    if not os.path.exists(newpath):
        print("Folder created")
        return True


def test_fixture(create_directories):
    print("Fixture executed")
