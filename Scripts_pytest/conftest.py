import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options



#Appium
#from appium import webdriver


# To Run parallel execution
# pip install pytest-xdist


@pytest.fixture(scope="function")
def browser_fun(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
    driver.maximize_window()
    request.instance.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()


@pytest.fixture(scope="class")
def browser_cls(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
    driver.maximize_window()
    request.cls.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()  



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser")
    parser.addoption("--headless", action="store", help="input headless")


@pytest.fixture()
def params(request):
    params = {}
    params['browser'] = request.config.getoption('--browser')
    params['headless'] = request.config.getoption('--headless')
    return params


@pytest.fixture()
def multiple_browser(request, params):
    web_driver = ""
    if params['browser'] == 'chrome':
        if params['headless'] == 'True':
            #options = Options()
            #options.add_argument('--headless')
            #options.add_argument('--disable-gpu')
            options = webdriver.ChromeOptions()
            options.headless = True
            web_driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver",options=options)
            web_driver.maximize_window()
        else:
            web_driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
            web_driver.maximize_window()


    if params['browser'] == 'firefox':
        if params['headless'] == 'True':
            options = webdriver.FirefoxOptions()
            options.headless = True
            web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
            web_driver.maximize_window()
        else:
            web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            web_driver.maximize_window()

    request.instance.driver = web_driver
    yield web_driver
    web_driver.close()


@pytest.fixture()
def jsonData():
    with open('TestData/testData.json') as config_file:
        data = json.load(config_file)
    return data

'''
@pytest.fixture()
def appiumdriver(request):
    print("initiating chrome driver")

    capabilities = {

        "deviceName":"Samsung Galaxy",
        "platformName":"Android",
        "platformVersion":"11.1",
        "browserName":"chrome",
        "udid":"11f2b948"
    }
    driver = webdriver.Remote("https://localhost:4723/wd/hub" , capabilities)
    request.instance.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()
    '''