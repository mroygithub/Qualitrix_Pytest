import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
from Scripts_pytest import conftest
import allure


# py.test Scripts_pytest/Test_google.py --html=Report/test.html --browser=chrome --headless=True
# py.test Scripts_pytest/Test_google.py --alluredir=Report/testAll.html --browser=chrome --headless=True


@pytest.mark.usefixtures("multiple_browser")
class TestGoogleApp:

    @pytest.mark.smoke
    def test_WEB_Alert(self,jsonData):


        self.driver.get(jsonData['url_heroku'])
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//a[text()='JavaScript Alerts']").click()
        self.driver.implicitly_wait(10)
        

        # Click on Click for JS Alert

        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        time.sleep(3)
        
        # create alert object 
        alert = Alert(self.driver)
        # get alert text 
        print(alert.text) 
        # accept the alert 
        alert.accept() 
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").is_displayed()
        time.sleep(3)

        
        
  
        


        #logo = self.driver.find_elements(By.XPATH, "//img[@alt='Google']")
        #assert len(logo) == 0

    @pytest.mark.regression
    def test_google_searchbox(self,jsonData):

        self.driver.get(jsonData['url_heroku'])
        self.driver.implicitly_wait(10)
        #logo = self.driver.find_elements(By.XPATH, "//img[@alt='Google']")
       # assert len(logo) > 0

    