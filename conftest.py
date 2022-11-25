import os
import pytest


@pytest.fixture(scope="session")
def create_directories():
    newpath = r'C:\\pytest'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


@pytest.fixture(autouse=True)
def os_dependencies_status():
    print("Status OK")
