import pytest


@pytest.mark.skip(reason="Skip the test cases for demonstration")
def test_skipped():
    print("This test cases should be skipped")
    assert False


def test_not_to_skipped():
    print("Test should be executed")
    assert True


@pytest.mark.skipif(True, reason="Conditionally skipping this test")
def test_skipped_if_condition():
    print("This test should also be skipped due to skip if condition")
    assert False  # This assert False line won't be executed due to skipping(skipif condition)
    # This assert False line is used to intentionally fail the test if it is executed
    # (which it won't be in this case because it's skipped).


@pytest.mark.skipif(False, reason="Conditionally skipping this test")
def test_skipped_if_condition():
    print("This test should also be skipped due to skip if condition")
    assert True  # This line will be executed since the test is not skipped


"""
@pytest.mark.skipif(True, ...) always skips the test.
@pytest.mark.skipif(False, ...) never skips the test.
"""


def test_skip_based_on_condition():
    should_skip = True  # Condition to skip the test
    if should_skip:
        pytest.skip("Skipping this test based on a condition")
    print("This test should be skipped based on a condition")
    assert False  # This line won't be executed due to skipping
