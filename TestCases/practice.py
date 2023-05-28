from selenium.webdriver.common.by import By
class EmployeeSearch:
    Text_EmpName_XPATH = "This is empname path"
    Click_Search_XPATH = (By.XPATH, "//button[@type='submit']")
    Search_Result_CSS = (By.CSS_SELECTOR,
                         "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)")

    def __init__(self, driver):
        self.driver = driver
        print(self.driver)

    def Enter_EmpName(self,Text_EmpName_XPATH):
        #self.Text_EmpName_XPATH=Text_EmpName_XPATH
        print(*EmployeeSearch.Text_EmpName_XPATH)
        print(Text_EmpName_XPATH)


oes=EmployeeSearch("edge")
oes.Enter_EmpName("milind")