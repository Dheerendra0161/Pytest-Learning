import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType


@pytest.fixture(autouse=True, scope="function")
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()



# @pytest.fixture(scope="function")
# def driver(request):
#     global driver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#
#     def teardown():
#         driver.quit()
#
#     request.addfinalizer(teardown)
#
#     return driver
