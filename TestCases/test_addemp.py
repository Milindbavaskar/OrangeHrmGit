import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.edge import webdriver
from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.AddEmp_Page import AddEmployee
from PageObjects.LoginPage import loginpage
from utilites.Logger import LogGenerator
from utilites.readproperties import Readconfig

class Test_Add_Emp:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_addEmp_003(self, setup):
        self.log.info("test_addEmp_003 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Going to Url-->" + self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering UserName-->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("Click On login")
        self.ae = AddEmployee(self.driver)
        self.ae.Click_PIM()
        self.log.info("Click On PIM")
        self.ae.Click_Add()
        self.log.info("Click On Add")
        time.sleep(2)
        self.ae.Enter_FirstName("Credence")
        self.log.info("Entering FirstName")
        self.ae.Enter_MiddleName("It")
        self.log.info("Entering MiddleName")
        self.ae.Enter_LastName("Pune")
        self.log.info("Entering LastName")
        time.sleep(2)
        self.ae.Click_Save()
        self.log.info("Click on Save")
        if self.ae.Add_Employee_stuats() == True:
            time.sleep(2)
            self.driver.save_screenshot(
                "C:\\Users\\admin\\PycharmProjects\\OrangeHrmProject\\Screenshots\\test_addEmp_003-pass.png")
            self.lp.Click_MenuButton()
            self.log.info("Click on MenuButton")
            self.lp.Click_Logout()
            self.log.info("Click on Logout Button")
            assert True
            self.log.info("test_addEmp_003 is Passed")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\admin\\PycharmProjects\\OrangeHrmProject\\Screenshots\\test_addEmp_003-fail.png")
            self.log.info("test_addEmp_003 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_addEmp_003 is Completed")

# class Test_Add_Emp:
#     def test_addEmp_003(self):
#         driver = webdriver.Edge()
#         driver.implicitly_wait(10)
#         driver.get("https://opensource-demo.orangehrmlive.com/")
#         driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
#         driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
#         driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
#         driver.find_element(By.XPATH,
#                              "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space("
#                              ")='PIM']").click()
#         driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
#         driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Credence")
#         driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Credence")
#         driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Credence")
#         time.sleep(1)
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
#         try:
#           driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']")
#           print("test_addEmp_002 is Passed")
#           driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
#           driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
#           addemp = True
#         except Ec:
#            print("test_addEmp_002 is Failed")
#            print("test_addEmp_002 is completed")
#            addemp = False
#
#         if addemp == True:
#            assert True
#         else:
#            assert False
#         driver.close()




