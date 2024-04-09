import pytest

"""
Fixtures are a powerful feature of pytest that helps in writing well-structured and maintainable tests
"""

def test_login_with_valid_credential(setup_and_teardown):
    print("Enter valid email and password")


def test_login_with_invalid_credential(setup_and_teardown):
    print("Enter invalid email and password")



"""
fixture will run before each method or function
yield will run after each functions

Lunching the browser
Opening the the url
------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------- 
Enter invalid email and password
---------------------------------------------------------------------------- Captured stdout teardown ----------------------------------------------------------------------------- 
closing the browser

"""