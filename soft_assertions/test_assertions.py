import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
install -->  pip install pytest-soft-assertions
To run from the terminal --> pytest -vs --soft-asserts
it will convert hard into soft assertions
"""


@pytest.fixture
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.chiacon.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_chiacon(setup_and_teardown):
    actual_title = driver.title
    expected_title = "Chiacon2"
    assert actual_title.__eq__(expected_title)

    driver.find_element(By.XPATH,
                        "//span[contains(text(),'Contact Us') and @class='StylableButton2545352419__label wixui-button__label']").click()
    assert driver.find_element(By.XPATH, "//span[contains(text(),'Drop us message for any query')]").is_displayed()






