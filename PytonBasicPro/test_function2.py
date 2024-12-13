#import sys
#rom pathlib import Path
#sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Demo_Selenium1:


    def launch_Web_Application(self):
        global driver
        options = webdriver.ChromeOptions()
        options.headless = False
        driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver",options=options)
        driver.maximize_window()
        driver.get("https://www.docker.com")
        driver.implicitly_wait(20)

    
    def test_docker_HomePage_Scenarios(self):

        if driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....") 

        thisdict={"LinkPosition":"LinkName"}
        file1 = open("/Users/mithunroy/Desktop/VSCodePythonProject/Qualitrix/demo.txt", "w") 
        link_count = len(driver.find_elements(By.XPATH, "//a"))
        for i in range(1,link_count+1):
            Xpath = '(//a)['+str(i)+']'
            txt = driver.find_element(By.XPATH, Xpath).text
            thisdict.update({i: txt})
            file1.writelines("When position is:"+str(i)+"Then Link Text is:"+str(txt)+"\n")
        print(thisdict)  
        
        
        file1.close() 
        print("Data is written into the file.")

    

    def close_my_Application(self):

        driver.quit()

obj = Demo_Selenium1()

obj.launch_Web_Application()
obj.test_docker_HomePage_Scenarios()
obj.close_my_Application()


                