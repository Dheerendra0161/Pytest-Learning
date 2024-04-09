import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


# Parameterizing fixtures using params
@pytest.fixture()
# used to define a fixture that will run multiple times, each time with a different parameter.
def set_and_teardown(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def set_and_teardown_without_params(request):
    # Provide this name in the test cases @pytest.mark.usefixtures("set_and_teardown_without_params", "log_on_failure")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


# Take screen shout only in cases of the failure of the test
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="zoho screenShot",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    return report
