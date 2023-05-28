import time
from PageObjects.AddEmp_Page import AddEmployee
from PageObjects.LoginPage import loginpage
from utilites import XLUtils
from utilites.Logger import LogGenerator
from utilites.readproperties import Readconfig


class Test_Add_Emp_DDT:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "C:\\Users\\admin\\PycharmProjects\\OrangeHrmProject\\TestData\\New Microsoft Excel Worksheet.xlsx"


    def test_addEmp_ddt_005(self, setup):
        self.log.info("test_addEmp_ddt_005 is started")
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
        self.rows = XLUtils.getrowCount(self.path, 'Sheet1')
        print("Number of rows are --->", self.rows)
        self.ae.Click_PIM()
        self.log.info("Click On PIM")
        self.ae.Click_Add()
        self.log.info("Click On Add")
        status_list= []
        for r in range(2, self.rows+1):
            self.FirstName = XLUtils.readData(self.path, 'Sheet1',r, 1)
            self.MiddleName = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.LastName = XLUtils.readData(self.path, 'Sheet1', r, 3)
            #time.sleep(2)
            self.ae.Enter_FirstName(self.FirstName)
            self.log.info("Entering FirstName-->" + self.FirstName)
            self.ae.Enter_MiddleName(self.MiddleName)
            self.log.info("Entering MiddleName-->" + self.MiddleName)
            self.ae.Enter_LastName(self.LastName)
            self.log.info("Entering LastName--> "+ self.LastName)
            time.sleep(2)
            self.ae.Click_Save()
            self.log.info("Click on Save")
            if self.ae.Add_Employee_stuats() == True:
                self.ae.Click_AddEmployee()
                # time.sleep(2)
                status_list.append("Pass")
                XLUtils.writeData(self.path, 'Sheet1', r, 4,"Pass")
                #self.driver.save_screenshot(
                   # "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\test_addEmp_003-pass.png")

            else:
                status_list.append("Fail")
                XLUtils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                #self.driver.save_screenshot(
                    #"D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\test_addEmp_003-fail.png")


        print(status_list)

        time.sleep(2)
        self.lp.Click_MenuButton()
        self.log.info("Click on MenuButton")
        self.lp.Click_Logout()
        self.log.info("Click on Logout Button")
        self.driver.close()
        if "Fail" not in status_list:
            self.log.info("test_addEmp_ddt_005 is Passed")
            assert True
        else:
            self.log.info("test_addEmp_ddt_005 is Failed")
            assert False
        self.log.info("test_addEmp_ddt_005 is Completed")