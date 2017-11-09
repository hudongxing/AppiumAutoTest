import unittest
import TestCases.common.Initialize as initialize
from utils.Element import *
from time import sleep
from TestCases.common.Token import getShortList, getAplist
import random
from TestCases.common.CutScreenshot import cutScreenShot
from config import Config
from TestCases.common.InitMySql import operationMySql


class SYMain(unittest.TestCase):
    driver = None
    token = None

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.driver = initialize.setUp()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        initialize.tearDown(self)

    def test_Transport(self):
        if getShortList("传输列表"):
            get_xpath(self, "//*[@text='传输列表']").click()
            if find_toast('正在加载...', self.driver):
                pass
            try:
                get_id(self, "com.unicocloud.smarthome:id/transfer_download").click()

                self.assertTrue(True)

            except:

                self.assertTrue(False)
        else:
            self.assertTrue(False, "Token获取失败")

    def test_router_ap(self):
        if getShortList("路由器"):
            get_xpath(self, "//*[@text='路由器']").click()
            get_id(self, "com.unicocloud.smarthome:id/llt_wireless_setting").click()
            get_id(self, "com.unicocloud.smarthome:id/llt_signal_intensity").click()
            get_id(self, "com.unicocloud.smarthome:id/balance_mode").click()
            index = getAplist()
            xpath = "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index,%s)]" % (
                index - 1,)
            get_xpath(self, xpath).click()
            try:
                get_id(self, "com.unicocloud.smarthome:id/llt_hard_version")
                self.assertTrue(True)
            except:
                cutScreenShot(self, "AP界面截图")
                self.assertTrue(False)

        else:
            self.assertTrue(False, "Token获取失败")

    def test_router_access(self):
        if getShortList("路由器"):
            get_xpath(self, "//*[@text='路由器']").click()
            get_id(self, "com.unicocloud.smarthome:id/llt_access_user").click()
            try:
                get_id(self, "com.unicocloud.smarthome:id/rv_online_devices")
                self.assertTrue(True)
            except:
                self.assertTrue(False)
        else:
            self.assertTrue(False, "Token获取失败")

    def test_add(self):
        if getShortList("添加设备"):
            sleep(5)
            try:
                get_xpath(self, "//*[@text='添加设备']").click()
                get_xpath(self, "//*[@text='添加红外设备']").click()
                get_xpath(self,
                          "//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[contains(@index,0)]").click()
                get_id(self, "com.unicocloud.smarthome:id/btn_next").click()
                cutScreenShot(self, "设备列表混乱")
                self.assertTrue(True)
            except:
                cutScreenShot(self, "设备列表混乱")
                self.assertTrue(False)
        else:
            cutScreenShot(self, "添加设备按钮不存在")
            self.assertTrue(False, Config.messageFalse)

    def test_user(self):
        if getShortList("用户管理"):
            sleep(5)
            get_xpath(self, "//*[@text='用户管理']").click()
            get_id(self, "com.unicocloud.smarthome:id/user").click()
            t = get_id(self, "com.unicocloud.smarthome:id/tv_phone_number").text
            self.assertEqual(t, "18801184375", "手机号显示不正确")
        else:
            cutScreenShot(self, "用户管理按钮不存在")
            self.assertTrue(False, Config.messageFalse)

    def test_message(self):
        sleep(3)
        get_id(self, "com.unicocloud.smarthome:id/news_wrapper").click()
        try:
            get_xpath(self, "//*[@text='新用户加入']")
            self.assertTrue(True)
        except:
            cutScreenShot(self, "消息中心截图")
            self.assertTrue(False)

    def test_pager_source(self):

        print(self.driver.current_activity())
