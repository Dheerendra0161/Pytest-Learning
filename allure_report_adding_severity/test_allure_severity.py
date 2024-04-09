from allure_commons.types import AttachmentType
import allure
from allure_report_adding_severity.severity_decorator import severity

"""
install-->      pip install pytest-xdist
number of test function to run in parallel-->   pytest - n 5       
two-two function will run in parallel   -->pytest -n 2 test_parallel_browser_run.py    

"""


class TestMultiBrowser:
    # @severity("blocker")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_launch_browser1(self):
        self.driver.get("https://www.chiacon.com/")

    # @severity("critical")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_launch_browser2(self):
        self.driver.get("https://www.amazon.com/")

    # @severity("normal")
    @allure.severity(allure.severity_level.NORMAL)
    def test_launch_browser3(self):
        self.driver.get("https://www.flipkart.com/")

    # @severity("minor")
    @allure.severity(allure.severity_level.MINOR)
    def test_launch_browser4(self):
        self.driver.get("https://www.zoho.com/people/logout.html")
        allure.attach(self.driver.get_screenshot_as_png(), name="zohoLandingPageScreenshot",
                      attachment_type=AttachmentType.PNG)

    # @severity("trivial")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_launch_browser5(self):
        self.driver.get("https://coverzoo.com/")


"""
Running individual test in pytest using pycharm option
settings:
Select project--> 3 line bar -->setting -->Tools -->Python Integrate Tool -->Testing --> Pytest
"""

"""

Allure reports use severity levels to indicate the importance of a test failure.  This helps prioritize bugs and focus attention on the most critical issues.

There are five predefined severity levels in Allure:

Blocker: This is the most severe level, indicating a critical issue that completely prevents the application from functioning
Critical: This indicates a severe issue that makes a core feature unusable
Normal: This is the default level for failing tests. It represents a significant issue that should be addressed
Minor: This indicates a less critical issue, such as a minor UI bug
Trivial: This is the least severe level, representing a very minor issue that may not even be noticeable to users


"""
