import pytest


# Grouping Tests in python

@pytest.mark.smoke
def test_message1():
    print("Functions:smoke")


@pytest.mark.regression
def test_message2():
    print("Functions:regression")


@pytest.mark.smoke
def test_message3A():
    print("Functions:smoke")


def test_message4():
    print("How are you Boss3")


@pytest.mark.smoke
def test_message5():
    print("Functions:smoke")


@pytest.mark.regression
def test_message6():
    print("Functions:regression")


@pytest.mark.regression
def test_message7():
    print("Functions:regression")


# test_message1()
# test_message2()
# test_message3A()
# test_message4()
# test_message5()
# test_message6()
# test_message7()

# To run specific package in specific file in specific function
#  Change the directory cd package_name
# eg.   pytest - vs - k "test_grouping.py" - m smoke

# Run methods from command line
#  pytest -m smoke
#  pytest -m regression
