import pytest
"""
project/
|-- conftest.py         <-- Global fixtures and hooks
|-- tests/
|   |-- conftest.py     <-- Fixtures and hooks for the 'tests' directory
|   |-- test_file1.py
|   |-- test_file2.py
|-- utils/
|   |-- conftest.py     <-- Fixtures and hooks for the 'utils' directory
|   |-- test_utils.py

"""



@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("Lunching the browser")
    print("Opening the the url ")
    yield
    print("closing the browser")
