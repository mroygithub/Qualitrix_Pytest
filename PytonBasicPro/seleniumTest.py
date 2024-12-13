#import sys
#rom pathlib import Path
#sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest


@pytest.fixture(scope="function")
def browser_Ch(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
    driver.maximize_window()
    driver.get("https://www.docker.com")
    driver.implicitly_wait(20)
    request.instance.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()


@pytest.fixture(scope="class")
def browser_cls(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
    driver.maximize_window()
    driver.get("https://www.docker.com")
    driver.implicitly_wait(20)
    request.cls.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()    

@pytest.mark.usefixtures("browser_cls")
class TestDemo_Selenium():

    
    def test_docker_HomePage_Scenarios(self):

        self.driver.get("https://www.docker.com")
        self.driver.implicitly_wait(20)

        if self.driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....") 


    def test_docker_HomePage_Scenarios1(self):

        self.driver.get("https://www.docker.com")
        self.driver.implicitly_wait(20)
        if self.driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....")  


    def test_docker_HomePage_Scenarios3(self):

        if self.driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....")                
    

 




                