import unittest
import TestCases.common.Initialize as initialize
from utils.Element import *
from time import sleep
import random
from TestCases.common.CutScreenshot import cutScreenShot
from config import Config
from TestCases.common.InitMySql import operationMySql


class SYCocloud(unittest.TestCase):
    driver = None
    cursor = None

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

    # 图片
    def test_image(self):
        sleep(10)
        get_xpath(self, "//*[@text='私有云']").click()
        # 点击图片
        get_id(self, "com.unicocloud.smarthome:id/file_photo_relativelayout").click()
        # 点击我的文件
        get_id(self, "com.unicocloud.smarthome:id/ll_my_file").click()
        get_id(self, "com.unicocloud.smarthome:id/rl_pop_file").click()
        # 点击多选
        get_id(self, "com.unicocloud.smarthome:id/tv_more").click()
        # 全选
        get_id(self, "com.unicocloud.smarthome:id/tv_selecte").click()
        # 下载
        get_id(self, "com.unicocloud.smarthome:id/rl_down").click()
        if find_toast("下载任务已追加,详细请查看传输列表", self.driver):
            self.assertTrue(True, "下载进行中")
        else:
            self.assertTrue(False, "下载失败")

    def test_video(self):
        sleep(5)
        get_xpath(self, "//*[@text='私有云']").click()
        get_id(self, "com.unicocloud.smarthome:id/file_video_relativelayout").click()
        self.driver.implicitly_wait(5)
        try:
            # 播放第一个视频
            get_xpath(self,
                      "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[contains(@index,0)]").click()
            sleep(10)
        except:
            cutScreenShot(self, "test_video")
            self.assertTrue(False, Config.messageFalse)

    # 文件管理
    def test_management(self):
        text = None
        sleep(5)
        try:
            get_xpath(self, "//*[@text='私有云']").click()
            get_id(self, "com.unicocloud.smarthome:id/file_all_relativelayout").click()
            get_id(self, "com.unicocloud.smarthome:id/flow_buttom").click()
            # 新建文件夹
            sleep(3)
            get_id(self, "com.unicocloud.smarthome:id/creat_layout").click()
            text = "醉红颜" + str(random.randint(12, 100))
            get_id(self, "com.unicocloud.smarthome:id/et_value").send_keys(text)
            get_id(self, "com.unicocloud.smarthome:id/tv_ok").click()
        except:
            pass
        if operationMySql(text):
            self.assertTrue(True, Config.messageTrue)
        else:
            cutScreenShot(self, "创建文件夹失败")
            self.assertTrue(False, Config.messageFalse)

    # 其他
    def test_other(self):
        sleep(5)
        get_xpath(self, "//*[@text='私有云']").click()
        get_id(self, "com.unicocloud.smarthome:id/file_other_relativelayout")
