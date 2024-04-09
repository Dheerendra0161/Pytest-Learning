def test_addition():
    x, y = 9, 5
    assert x + y == 14


def test_compare():
    x, y = 9, 5
    assert x > y


def test_equality():
    x, y = 9, 5
    assert x.__eq__(y), 'Given values are not equal'  # Message can be reflected in the output
