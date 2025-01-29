import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.loginPage import login
from pageObjects.addCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from testCases.conf_test import setup
from utilities.customLogger import LogGen
from selenium import webdriver
import string
import random

class Test_addCustomer:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity  # group the test cases
    def test_addCustomer(self,setup):
        self.logger.info("*********Test_addCustomer*******")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("*****Login successful*******")

        #Add Customer Test
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("*****Providing customer info******")
        self.email = random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setFirstName("Jayanth")
        self.addcust.setLastName("chidanand")
        self.addcust.setCompanyName("TestYantra")
        self.addcust.clickOnSave()

        self.logger.info("******Saving Customer info*****")
        self.logger.info("*******Add Customer validation started******")

        #self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        #print(self.msg)
        if 'customer has been added successfully' in self.msg:
            assert True == False
            self.logger.info("*****Add customer Test Passed******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")   #Screenshot
            self.logger.error("******Add Customer Test Failed******")
            assert True == False

        self.driver.close()
        self.logger.info("*****Ending Home Page Title Test******")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

