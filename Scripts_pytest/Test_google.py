import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


# py.test Scripts_pytest/Test_google.py --html=Report/test.html --browser=chrome --headless=True


@pytest.mark.usefixtures("multiple_browser")
class TestGoogleApp:

    # Set up the logger
    global logger
    logger = logging.getLogger(__name__)

    @pytest.mark.smoke
    def test_google_logo(self,jsonData):

        self.driver.get(jsonData['url_google'])
        self.driver.implicitly_wait(10)
        logo = self.driver.find_elements(By.XPATH, "//img[@alt='Google']")
        assert len(logo) == 0
        logger.info("Test case 001 is PASS ................")

    @pytest.mark.regression
    def test_google_searchbox(self,jsonData):

        self.driver.get(jsonData['url_google'])
        self.driver.implicitly_wait(10)
        logo = self.driver.find_elements(By.XPATH, "//img[@alt='Google']")
        assert len(logo) > 0
        logger.info("Test case 001003 is FAIL ................")

    