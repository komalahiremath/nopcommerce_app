import time
from tkinter.tix import Select

from selenium import webdriver
from selenium.webdriver.common.by import By


class AddCustomer:
    #Add Customer page
    lnkCustomer_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomer_item_xpath="//a[@href='/Admin/Customer/List']"
    button_add_customer_xpath="//a[normalize-space()='Add new']"
    email_textbox_xpath="//input[@id='Email']"
    password_textbox_xpath="//input[@id='Password']"
    firstName_textbox_xpath = "//input[@id='FirstName']"
    lastName_textbox_xpath = "//input[@id='LastName']"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath="//input[@id='DateOfBirth']"
    txtCompany_name_xapth="//input[@id='Company']"
    txtCustomer_roles_xpath="//span[@aria-expanded='true']//input[@role='searchbox']"
    drpmgrOfVendor_xpath="//select[@id='VendorId']"
    btnSave_xpath="//button[@name='save']"
    lstitemRegistered_xpath = "//*[@id='select2-SelectedCustomerRoleIds-result-5mkv-3']"
    lstitemAdministractors_xpath = '//*[@id="select2-SelectedCustomerRoleIds-result-29ar-1"]'
    lstitemGuests_xpath = "//*[@id='select2-SelectedCustomerRoleIds-result-cxqp-4']"
    lstitemVendors_xpath = "//select[@id='VendorId']"


    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_item_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.button_add_customer_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_textbox_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.password_textbox_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.firstName_textbox_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.lastName_textbox_xpath).send_keys(lastname)

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompany_name_xapth).send_keys(comname)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomer_roles_xpath).send_keys(role)
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Administractors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdministractors_xpath)
        elif role == 'Guests':
            # here user can be Registered (or) Guest, only one
            time.sleep(3)
            #enselect the registered
            self.driver.find_element(By.XPATH,"//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
        drp.selectByVisibleText(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()





