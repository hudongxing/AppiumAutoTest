
from utils.Element import *


def init_login(self):
    # 处理登陆流程
    print("APP启动============开始执行登陆")
    get_id(self, 'com.android.packageinstaller:id/permission_allow_button').click()
    self.driver.implicitly_wait(2)
    get_id(self, 'com.android.packageinstaller:id/permission_allow_button').click()
    self.driver.implicitly_wait(2)
    swipeLeft(self, 800)
    swipeLeft(self, 800)
    swipeLeft(self, 800)
    swipeLeft(self, 800)
    self.driver.implicitly_wait(2)
    get_id(self, "com.unicocloud.smarthome:id/start_ehome").click()
    get_id(self, 'com.unicocloud.smarthome:id/user_name').send_keys("18801184375")
    self.driver.implicitly_wait(2)
    get_id(self, 'com.unicocloud.smarthome:id/user_password').send_keys("Aa111111")
    self.driver.implicitly_wait(2)
    get_id(self, "com.unicocloud.smarthome:id/sign_in_button").click()

def getSize(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    return x, y

def swipeLeft(self, t):
    l = getSize(self)
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.25)
    self.driver.swipe(x1, y1, x2, y1, t)
