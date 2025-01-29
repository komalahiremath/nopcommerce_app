import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import login
from testCases.conf_test import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_login_DDT:
    baseURL=ReadConfig.getURL()
    path=".//TestData/Login_Data.xlsx"
    #username=ReadConfig.getUserEmail()
    #password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("***************Test_login_DDT*************************")
        self.logger.info("***************Verifying login test*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=login(self.driver)
        time.sleep(2)
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows:",self.rows)

        lst_status=[]     #Empty list variable

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1 )
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.ClickLogin()
            time.sleep(2)
            act_title = self.driver.title
            self.driver.close()
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("*****Passed****")
                    self.lp.ClickLogout()
                    lst_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.info("*****Failed****")
                    self.lp.ClickLogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=='Pass':
                    self.logger.info("*****Failed****")
                    self.lp.ClickLogout()
                    lst_status.append("Fail")
                elif self.exp=='Fail':
                    self.logger.info("*****Passed****")
                    self.lp.ClickLogout()
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                self.logger.info("***Login DDT passed*****")
                self.driver.close()
                assert True
            else:
                self.logger.info("***Login DDT Failed*****")
                self.driver.close()
                assert False


        self.logger.info("******End of Login DDT Login_Test******")







        #self.lp.bypass()
        time.sleep(5)

        self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************login test is passed*************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_login.png")
            self.logger.error("***************login title test is failed*************************")
            assert False


