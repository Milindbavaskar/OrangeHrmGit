import time

from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.LoginPage import loginpage

from utilites.readproperties import Readconfig
from utilites.Logger import LogGenerator


class Test_login:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_title_001(self,setup):
        self.driver=setup
        self.log.info("test_Page_Title_001 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)
        #driver=webdriver.Edge()
        self.driver.implicitly_wait(10)
        #driver.get("https://opensource-demo.orangehrmlive.com/")
        if self.driver.title=="OrangeHRM":
            #print(self.driver.title)
            assert True
            self.log.info("test_Page_Title_001 is Passed")
            self.log.info("Page Title is-->" + self.driver.title)
        else:
            self.log.info("test_Page_Title_001 is Failed")
            assert False
            #self.log.info("test_Page_Title_001 is Failed")

        self.driver.close()
        self.log.info("test_Page_Title_001 is completed")

    def test_login_002(self,setup):  #no need to provide browser and site name again
        self.driver=setup
        self.log.info("test_login_002 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)
        #driver = webdriver.Edge()
        #driver.get("https://opensource-demo.orangehrmlive.com/")
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName("Admin")
        self.log.info("Entering username-->" + self.username)
        #time.sleep(5)
        #driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.lp.Enter_Password("admin123")
        self.log.info("Entering password-->" + self.password)
        self.log.info("Click on login button")
        #driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.lp.Click_Login()
        #driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # time.sleep(5)
        # try:
        #     driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        #     #print("test_login_002 is Passed")
        #     driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        #     driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #     print("test_login_002 is Passed")
        #     login = True
        #     #assert True
        #     print(login)
        # except Ec:
        #     print("test_login_002 is Failed")
        #     print("test_login_002 is completed")
        #     login = False
        #     print(login)
        #     #assert False
        # if login == True:
        #     assert True
        # else:
        #     assert False
        if self.lp.Login_Status() == True:
            self.driver.save_screenshot(
                "C:\\Users\\admin\\PycharmProjects\\OrangeHrmProject\\Screenshots\\test_login_002-pass.png")
            self.lp.Click_MenuButton()
            self.log.info("Click on Menu button")
            self.lp.Click_Logout()
            self.log.info("Click on logout button")
            self.log.info("test_login_002 is Passed")
            assert True
        else:
            self.log.info("test_login_002 is Failed")
            self.driver.save_screenshot(
                "C:\\Users\\admin\\PycharmProjects\\OrangeHrmProject\\Screenshots\\test_login_002-pass.png")
            assert False

        self.driver.close()
        self.log.info("test_login_002 is Completed")
