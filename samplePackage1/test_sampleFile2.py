import pytest
"""
Custom Markers:
You can define custom markers in your test files using the @pytest.mark decorator.
@pytest.mark.smoke
@pytest.mark.regression
Command to run specific mark
    pytest -m smoke
    pytest -m regression
    pytest -m "smoke or regression"          --->logical OR.
    
    
    pytest -m "not smoke"               --- exclusion of smoke


To run specific file  lets take test_sampleFile2.py
    pytest -m smoke test_sampleFile2.py
    pytest -m "smoke or regression" test_sampleFile2.py



The PytestUnknownMarkWarning occurs when pytest encounters an unknown marker
in your test files. This warning is typically displayed when you have defined custom 
markers in your test files, but pytest does not recognize them because they are not registered.
Option 1: Register Custom Markers:
[pytest]
markers =
    smoke: mark a test as smoke test
    regression: mark a test as regression test
Option 2: Disable the Warning:
        pytest -p no:unknown-markers
    



"""

@pytest.mark.smoke
def test_print_hello():
    print("Hello, World!")


@pytest.mark.regression
def test_print_numbers():
    for i in range(1, 6):
        print(i)


@pytest.mark.smoke
def test_print_message():
    print("Hello I am Dheerendra")


# test_print_hello()
# test_print_numbers()
# test_print_message()




