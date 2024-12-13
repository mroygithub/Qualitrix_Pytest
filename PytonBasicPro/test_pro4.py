import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color
import time
from PytonBasicPro import common

class Experiment1:

    name = "RAMA"


    def test002(self):

        try:
            print("This is test002")
            global driver
            options = webdriver.ChromeOptions()
            options.headless = False
            driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver",options=options)
            driver.maximize_window()
            driver.get("https://stackify.com/")
            driver.implicitly_wait(20)
            time.sleep(10)
            color1 = driver.find_element(By.XPATH , "(//a[text()='Start Free Trial'])[2]").value_of_css_property("color")
            print(color1)
            BGcolor1 = driver.find_element(By.XPATH , "(//a[text()='Start Free Trial'])[2]").value_of_css_property("background-color")
            print(BGcolor1)


            # Get the TXT color ....

            txtColor = Color.from_string(color1).hex
            BGtxtColor = Color.from_string(BGcolor1).hex
            print(txtColor)
            print(BGtxtColor)
            print(common.color_code(txtColor))
            print(common.color_code(BGtxtColor))

            driver.quit()
        except:
            driver.quit()



   

obj = Experiment1()        

obj.test002()       





