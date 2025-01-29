from selenium import webdriver
from selenium.webdriver.common.by import By
#from seleniumbase import Driver

class login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)


    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    #def bypass(self):
        # pip3 install seleniumbase
        # initialize the driver in GUI mode with UC enabled
        #self.driver= Driver(uc=True, headless=False)

    def ClickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

