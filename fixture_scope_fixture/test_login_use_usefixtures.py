import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")  # Keep here function name setup_and_teardown
class TestUseFixtures:
    def test_chiacon_site(self):
        actual_title = self.driver.title
        expected_title = "Chiacon"
        assert actual_title == expected_title
        self.driver.find_element(By.XPATH,
                                 "//span[contains(text(),'Contact Us') and @class='StylableButton2545352419__label wixui-button__label']").click()
        assert self.driver.find_element(By.XPATH,
                                        "//span[contains(text(),'Drop us message for any query')]").is_displayed()
