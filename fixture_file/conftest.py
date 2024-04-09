import pytest

"""
A fixture in pytest is a function that provides data, objects, or resources 
to test functions. Fixtures are defined in test files and can be shared across 
test functions. Fixtures can help simplify test code and make tests more modular and reusable.
"""


@pytest.fixture()
def setup_and_teardown():
    print("Lunching the browser")
    print("Opening the the url ")
    yield
    print("closing the browser")




def my_generator():
    yield "Dheerendra"
    yield 2
    yield 3

# gen = my_generator()
#
# print(next(gen))  # Outputs: Dheerendra
# print(next(gen))  # Outputs: 2
# print(next(gen))  # Outputs: 3

# It is similar to java iterator.
