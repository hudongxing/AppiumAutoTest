"""封装元素"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def get_id(self, id):
    element = self.driver.find_element_by_id(id)
    return element


def get_name(self, name):
    element = self.driver.find_element_by_name(name)
    return element


def get_xpath(self, xpath):
    element = self.driver.find_element_by_xpath(xpath)
    return element

# toast方法
def find_toast(message, driver):
    try:
        message = '//*[@text=\'{}\']'.format(message)
        element = WebDriverWait(driver, 10, 0.5).until(
            expected_conditions.presence_of_element_located((By.XPATH, message)))
        return True
    except:
        return False

def swich_popwindow(message, driver):
    try:
        message = '//*[@text=\'{}\']'.format(message)
        element = WebDriverWait(driver, 10, 0.5).until(
            expected_conditions.presence_of_element_located((By.XPATH, message)))
        return element
    except:
        return False

