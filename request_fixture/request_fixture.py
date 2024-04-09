import pytest


# Fixture with function scope
@pytest.fixture(scope="function")
def my_fixture(request):
    print("\nSetting up for the test:", request.function.__name__)
    if hasattr(request, 'param'):
        print("Test parameters:", request.param)
    yield
    print("Tearing down after the test:", request.function.__name__)


# Test function with parametrization
@pytest.mark.parametrize("input_value, expected_output", [(1, 2), (3, 6)])
def test_multiply(my_fixture, input_value, expected_output):
    result = input_value * 2
    assert result == expected_output


# Running the test
"""
            First Parameter
request_fixture.py::test_multiply[1-2] 
Setting up for the test: test_multiply
Tearing down after the test: test_multiply
            
            Second Parameter
request_fixture.py::test_multiply[3-6] 
Setting up for the test: test_multiply
Tearing down after the test: test_multiply

"""
