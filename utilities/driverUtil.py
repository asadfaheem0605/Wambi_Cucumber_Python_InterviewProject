from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utilities.settings import settings

# driver = webdriver.Chrome('chromedriver.exe')
# wait = WebDriverWait(driver, 10)

class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None
    browser = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        nodeUrl = 'http://192.168.1.245:4444/wd/hub'
        print('---------' + settings.browser + '---------')
        if settings.browser == "chrome":
            self.driver = webdriver.Remote(command_executor=nodeUrl,
                                           desired_capabilities={'browserName': 'chrome',
                                                                 'javascriptEnabled': True})
        elif settings.browser == "firefox":
            self.driver = webdriver.Remote(command_executor=nodeUrl,
                                           desired_capabilities={'browserName': 'firefox',
                                                                 'javascriptEnabled': True})

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)

    def navigateToMaps(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def waitOnElement(self, elemXpath):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, elemXpath)))

    def waitFor(self, timeInSec):
        self.driver.implicitly_wait(timeInSec)

    def elementClick(self, elemXpath):
        return self.driver.find_element_by_xpath(elemXpath).click()

    def clearElement(self, elemXpath):
        return self.driver.find_element_by_xpath(elemXpath).clear()

    def enterValues(self, elemXpath, value):
        return self.driver.find_element_by_xpath(elemXpath).send_keys(value)

    def getTextForElement(self, element):
        return self.driver.find_element_by_xpath(element).text

    def getElements(self, element):
        return self.driver.find_elements_by_xpath(element)

    def switchWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def closeBrowser(self):
        self.driver.quit()

driver = Driver.get_instance()