"""
install-->      pip install pytest-xdist
number of test function to run in parallel-->   pytest - n 5       
two-two function will run in parallel   -->pytest -n 2 test_parallel_browser_run.py    

"""
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.mark.usefixtures("set_and_teardown")
class TestBrowserLaunch:

    def test_launch_browser1(self):

        self.driver.get("https://www.chiacon.com/")

    def test_launch_browser2(self):
        self.driver.get("https://www.amazon.com/")

    def test_launch_browser3(self):
        self.driver.get("https://www.flipkart.com/")

    def test_launch_browser4(self):
        self.driver.get("https://coverzoo.com/")

    def test_launch_browser5(self):
        self.driver.get("https://www.zoho.com/people/logout.html")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='zrating meh']")))
        element.click()
