import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import login
from testCases.conf_test import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_login:
    baseURL=ReadConfig.getURL()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity           #group the test cases
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("***************Test_login*************************")
        self.logger.info("***************Verifying home page title*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
            self.logger.info("***************home page title test is passed*************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Test_homePage.png")
            self.logger.error("***************home page title test is failed*************************")
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***************Verifying login test*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=login(self.driver)
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.ClickLogin()
        #self.lp.bypass()
        time.sleep(5)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************login test is passed*************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_login.png")
            self.logger.error("***************login title test is failed*************************")
            assert False


