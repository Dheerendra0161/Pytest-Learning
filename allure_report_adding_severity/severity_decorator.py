# Custom decorator for severity levels
import allure
import pytest


# Custom decorator for severity levels
# Custom decorator for severity levels
import allure


def severity(sev_level):
    def decorator(func):
        if sev_level == "blocker":
            allure.severity(allure.severity_level.BLOCKER)
        elif sev_level == "critical":
            allure.severity(allure.severity_level.CRITICAL)
        elif sev_level == "normal":
            allure.severity(allure.severity_level.NORMAL)
        elif sev_level == "minor":
            allure.severity(allure.severity_level.MINOR)
        elif sev_level == "trivial":
            allure.severity(allure.severity_level.TRIVIAL)
        else:
            raise ValueError("Invalid severity level")

        return func

    return decorator

# Usage example with severity decorator
# @severity("blocker")
# @allure.feature("Login")
# @allure.story("Invalid Credentials")
# def test_invalid_login():
#     # Test logic here
#     assert False, "Simulating a failed test due to invalid login"
