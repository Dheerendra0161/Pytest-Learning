import pytest

"""
Testng annotations, such as @BeforeTest, @AfterTest, @BeforeMethod, and @AfterMethod, provide
similar functionality to pytest's hooks and fixtures

Function Scope:

A fixture with function scope will run once for each test function.
It is the default scope if you don't specify any.
Useful when you want fresh data or setup for each test function.

Module Scope:

A fixture with module scope runs once for each module.
Useful when you want to prepare something once for all tests in a module.

Session Scope:

A fixture with session scope runs once for the entire test session.
Useful when you want to prepare something once for all tests in the entire test run.

"""


# Write these statement as it is.
# setup_module
# teardown_module
# setup_function
# teardown_function

def setup_module(module):  # This will run once before module functions.once for all tests in a module.
    print('\nRead the data from the excel file')


def teardown_module(module):  # This will run once after module functions.once for all tests in a module.
    print('\nSay this is the end of the project')


def setup_function(function):  # This will run before each functions
    print('\nLaunching the browser')


def teardown_function(function):  # This will run after each functions
    print('\nQuiting the browser')


def test1():
    print("\nThis is test 1")


def test2():
    print("This is test 2")

# Run from the terminal in pytest --> pytest -vs
