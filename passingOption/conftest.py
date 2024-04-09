import pytest
from selenium import webdriver


# Write this pytest_addoption as it is
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="CH", help="Specify the browser to run the tests")


@pytest.fixture()
def set_and_teardown(request):
    browser = request.config.getoption("--browser")
    if browser == "CH":
        driver = webdriver.Chrome()
    elif browser == "FF":
        driver = webdriver.Firefox()
    elif browser == "ED":
        driver = webdriver.Edge()
    else:
        raise ValueError("Invalid browser type")

    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()

# To run the specific function in a class -->
# pytest test_parallel_browser_run.py::TestBrowserLaunch::test_launch_browser1 --browser=ED
