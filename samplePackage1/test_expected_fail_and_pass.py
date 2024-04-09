import pytest


@pytest.mark.xfail(reason="Tests that are known to be broken but you still want to keep them in the test suite ")
def test_sample1():  # It will fail intentionally (due to assert False) but will be reported as an "expected failure" (XFAIL).
    print("inside sample 1")
    assert False  # This line will fail the test cases


@pytest.mark.skip(reason="To demonstrate the skipping")  # this code will be skipped
def test_sample2():
    print("inside sample 2")


@pytest.mark.xfail
def test_sample3():  # It will pass intentionally (due to assert True) but will be reported as an "expected pass" (XPASS).
    print("inside sample 3")
    assert True  # This line will pass the test cases
