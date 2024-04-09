import pytest
from selenium import webdriver

"""
function: The fixture is invoked once for each test function that uses it.
class: The fixture is invoked once per test class.
module: The fixture is invoked once per test module.
session: The fixture is invoked once per test session.

Testng annotations, such as @BeforeTest, @AfterTest, @BeforeMethod, and @AfterMethod, provide
similar functionality to pytest's hooks and fixtures

Function Scope:

A fixture with function scope will run once for each test function.
It is the default scope if you don't specify any.
Useful when you want fresh data or setup for each test function.

Class Scope: 
Pytest also supports organizing tests into classes. Test methods within
a class are also test functions, but they are grouped together within the class. 
This is useful for when you need setup and teardown logic for a group of tests.


Module Scope:

A fixture with module scope runs once for each module.
Useful when you want to prepare something once for all tests in a module.

Session Scope:

A fixture with session scope runs once for the entire test session.
Useful when you want to prepare something once for all tests in the entire test run.
# Running pytest at the command line starts a testing session
$ pytest



The autouse parameter in a Pytest fixture indicates that the fixture will be automatically 
invoked for each test function without explicitly passing it as an argument to the test functions. 
@pytest.fixture()
def setup_and_teardown():
     print("Hi")

No need of -->def test_login_with_invalid_credential(setup_and_teardown):

"""

# @pytest.fixture(autouse=True, scope='function')
# def setup_and_teardown():
#     print("Lunching the browser")
#     print("Opening the the url ")
#     yield
#     print("closing the browser")


# Fixture with different scopes
# @pytest.fixture(autouse=True, scope="function")
# def function_scope_fixture():
#     print("Before function")
#     yield
#     print("After function")


# @pytest.fixture(autouse=True, scope="class")
# def class_scope_fixture():
#     print("Before class")
#     yield
#     print("After class")


# @pytest.fixture(autouse=True, scope="module")
# def module_scope_fixture():
#     print("Before module")
#     yield
#     print("After module")


# @pytest.fixture(autouse=True, scope="session")
# def session_scope_fixture():
#     print("Before session")
#     yield
#     print("After session")





"""
In pytest, a request fixture is used to access information and resources related to the executing test. 
It provides information about the test function or class being executed, such as the name of the test, 
the module it belongs to, parameters passed to the test, and more.

When a test function or test method in a class requests the request fixture as an argument, pytest automatically 
provides it with information about the current test context.

"""


@pytest.fixture(scope="function")
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.get("https://www.chiacon.com/")
    driver.maximize_window()
    request.cls.driver = driver  # If you want to access the driver instance in the test class or method
    yield driver
    driver.quit()


"""
 Yield is a keyword that is used in the context of generator functions. When yield is used inside a function, 
 it turns that function into a generator. 
 Using yield allows the fixture to provide resources (like the WebDriver instance) to the test function.
"""

"""
you cannot have multiple conftest.py files within a single package. 
The conftest.py file is a mechanism provided by pytest to define hooks, 
fixtures, and other configurations that should be applied to a particular 
directory and all its subdirectories. This file is automatically discovered 
by pytest and applied to all tests in that directory and its subdirectories.


tests/
├── conftest.py  # This will apply to all tests in tests/ and its subdirectories
├── test_cases/
│   ├── conftest.py  # This will apply to tests in tests/test_cases/ and its subdirectories
│   ├── test_file1.py
│   └── test_file2.py
└── utilities/
    └── conftest.py  # This will apply to tests in tests/utilities/ and its subdirectories


The conftest.py in the root tests/ directory applies to all tests in tests/ and its subdirectories.
The conftest.py in tests/test_cases/ applies to tests in tests/test_cases/ and its subdirectories.
The conftest.py in tests/utilities/ applies to tests in tests/utilities/ and its subdirectories.
"""
