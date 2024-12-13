import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Locators import DockerLocators
from selenium.webdriver.common.by import By


class DockerPagefun:


    def __init__(self, driver):
        self.driver = driver


    
    
    def launch_app_with_url(self,url):
        # Put url in Chrome Browser ...
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Docker App is launched Successfully ... ..... PASS")


    def docker_logo_validation(self):
        # Click Text box tab
        assert len(self.driver.find_elements(By.XPATH, DockerLocators.dockerLogo())) == 1
        assert self.driver.find_element(By.XPATH, DockerLocators.dockerLogo()).is_displayed() == True
        print("Docker Logo is present ..... PASS")
        

    def login(self,testdata):
        # Click Text box tab
        self.driver.find_element_by_xpath("// label[text() = 'Scrolling']").click()
        # Enter the text in to the text box
        self.driver.find_element_by_id("username").send_keys(testdata)