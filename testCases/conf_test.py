from selenium import webdriver
import pytest




@pytest.fixture()
def setup():
    if browser=='edge':
        driver = webdriver.Ie()
    elif browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):         #This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

###############Pytest HTML Reports

#It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config.metadata['Project Name'] = 'nop commerce'
    config.metadata['Module Name'] = 'Customers'
    config.metadata['Tester'] = 'Komala'

# It is hook for adding environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)





    #def bypass():
        #driver = webdriver.Chrome()
        #element = driver.find_element(By.CSS_SELECTOR, "#px-captcha")
        #action = ActionChains(driver)
        #action.click_and_hold(element)
        #action.perform()