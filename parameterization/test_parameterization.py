import pytest


@pytest.mark.parametrize("username, password", [
    ("dheerendra1", "password1"),
    ("dheerendra2", "password2"),
    ("dheerendra3", "password3")
])
def test_login_with_valid_credential(username, password):
    print(username + " and " + password)
