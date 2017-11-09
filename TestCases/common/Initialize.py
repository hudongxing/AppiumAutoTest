from appium import webdriver
from config import Config


# 测试用例的初始化操作
def init_case(opt):
    print("Initialize")
desired_caps = Config.data
Driver = None
def setUp():
    global Driver
    Driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return Driver

def getDriver():
    return Driver

def tearDown(cls):
    Driver.quit()
    print('...........end .............. ')
