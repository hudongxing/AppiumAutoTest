import unittest
import TestCases.common.Initialize as initialize
from utils.Element import *
from time import sleep
import random
from TestCases.common.CutScreenshot import cutScreenShot
from config import Config
from TestCases.common.Token import *
import traceback

class MineTest(unittest.TestCase):
    driver = None

    # setUpClass方法在类初始化时仅调用一次
    @classmethod
    def setUpClass(cls):
        pass
        # 类初始化方法
        # cls.driver = initialize.Driver
        # if cls.driver is None:
        #     cls.driver = initialize.setUp()
        # print("----------------setUpClass-------------")

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.driver = initialize.setUp()
        print("----------------setup-------------")

    def tearDown(self):

        initialize.tearDown(self)
        print("-------------teardown------------------")
        # Initialize.tearDown(self)

    def test_mine(self):

        print("点击测试")

    # 我的按钮点击
    def test_account(self):
        try:
            sleep(5)
            get_xpath(self, "//*[@text='我的']").click()
            get_id(self, "com.unicocloud.smarthome:id/lly_user_name").click()
            get_id(self, "com.unicocloud.smarthome:id/lly_nick_name").click()
            get_id(self, "com.unicocloud.smarthome:id/et_user_nick_name").clear()
            get_id(self, "com.unicocloud.smarthome:id/et_user_nick_name").send_keys("醉红颜" + str(random.randint(12, 100)))
            get_id(self, "com.unicocloud.smarthome:id/setting").click()
            if find_toast('正在加载...', self.driver):
                print("正在加载")
            else:
                cutScreenShot(self, "test_account")
                self.assertEqual("截屏", "test", "修改用户名称失败")
            if find_toast('修改成功', self.driver):
                cutScreenShot(self, "test_account")
        except Exception as e:
            print(traceback.format_exc())
            cutScreenShot(self, "Fail_account")

    # 硬盘管理
    def test_hardDisk(self):
        try:
            sleep(10)
            get_xpath(self, "//*[@text='我的']").click()
            get_id(self, "com.unicocloud.smarthome:id/rl_route_room").click()
            get_id(self, "com.unicocloud.smarthome:id/img_title_left_back").click()
            t = get_id(self, "com.unicocloud.smarthome:id/tv_user_control").text
            self.assertEqual("用户管理", t, "测试失败了")
        except Exception as e:
            print(traceback.format_exc())
            cutScreenShot(self, "test_hardDisk")

    # 用户管理
    def test_user_management(self):

        sleep(5)
        get_xpath(self, "//*[@text='我的']").click()
        get_id(self, "com.unicocloud.smarthome:id/rl_user_control").click()
        if find_toast('正在加载...', self.driver):
            print("正在加载")
        else:
            cutScreenShot(self, "test_user_management")
        get_id(self, "com.unicocloud.smarthome:id/user").click()
        get_id(self, "com.unicocloud.smarthome:id/bt_logout").click()
        cutScreenShot(self, "注销截图")
        get_id(self, "com.unicocloud.smarthome:id/tv_left_button").click()

    # 修改头像
    def test_change_portrait(self):
        sleep(3)
        try:
            get_xpath(self, "//*[@text='我的']").click()
            get_id(self, "com.unicocloud.smarthome:id/rl_user_control").click()
            get_id(self, "com.unicocloud.smarthome:id/user").click()
            get_id(self, "com.unicocloud.smarthome:id/lly_head_portrait").click()
            if find_toast("手机相册", self.driver):
                print("已找到popwindow")
            get_xpath(self, "//*[@text='手机相册']").click()
            # self.driver.switch_to_alert()
            # get_id(self, "com.unicocloud.smarthome:id/tv_phone_photo_album").click()
            get_xpath(self, "//android.widget.ListView/android.widget.FrameLayout[1]").click()
            self.assertTrue(True)
        except:
            cutScreenShot(self, "选择相册失败")
            self.assertTrue(False)

    # 路由器管理
    def test_Router(self):

        sleep(5)
        get_xpath(self, "//*[@text='我的']").click()
        get_id(self, "com.unicocloud.smarthome:id/lly_router").click()
        # find_toast('正在加载...', 10, 0.5, self.driver)
        t = get_id(self, "com.unicocloud.smarthome:id/tv_internet_mode").text
        self.assertEqual("自动方式", t, Config.messageFalse)
        get_id(self, "com.unicocloud.smarthome:id/llt_wireless_setting").click()
        get_id(self, "com.unicocloud.smarthome:id/llt_wireless_setting").click()

        get_id(self, "com.unicocloud.smarthome:id/img_title_left_back").click()
        get_id(self, "com.unicocloud.smarthome:id/img_title_left_back").click()
        get_id(self, "com.unicocloud.smarthome:id/llt_router_upgrade").click()

        self.driver.implicitly_wait(10)
        if find_toast('正在加载...', self.driver):
            cutScreenShot(self, "test-server")
            # self.driver.keyevent(3)
            # self.driver.keyevent(3)
        else:
            print("toast已消失")

    # 系统设置
    def test_sys(self):

        sleep(5)
        get_xpath(self, "//*[@text='我的']").click()
        get_id(self, "com.unicocloud.smarthome:id/more_system_setting").click()
        get_id(self, "com.unicocloud.smarthome:id/rl_nick_name").click()
        get_id(self, "com.unicocloud.smarthome:id/et_nick_name").clear()
        get_id(self, "com.unicocloud.smarthome:id/et_nick_name").send_keys("醉红颜" + str(random.randint(12, 100)))
        get_id(self, "com.unicocloud.smarthome:id/setting").click()
        get_id(self, "com.unicocloud.smarthome:id/lly_local_space_clear").click()
        get_id(self, "com.unicocloud.smarthome:id/lly_cache_file").click()
        get_id(self, "com.unicocloud.smarthome:id/tv_right_button").click()
        if find_toast('清理完成', self.driver):
            cutScreenShot(self, "缓存文件为0")
        else:
            cutScreenShot(self, "清理缓存失败")
        # 返回系统设置界面
        get_id(self, "com.unicocloud.smarthome:id/iv_goback").click()
        # 意见反馈界面
        get_id(self, "com.unicocloud.smarthome:id/lly_feedback").click()

        # 判断意见反馈号码是否为当前手机号
        try:
            t = get_id(self, "com.unicocloud.smarthome:id/et_feedback_contactWay").text
            self.assertEqual(t, "18801184375", "反馈号码错误")
        except:

            cutScreenShot(self, "反馈账号")
        # 发送意见反馈
        get_id(self, "com.unicocloud.smarthome:id/et_feedback_content").send_keys("倾听你的声音，哈啊")
        get_id(self, "com.unicocloud.smarthome:id/tv_custom").click()

    # 检查更新
    def test_updata(self):

        sleep(5)
        get_xpath(self, "//*[@text='我的']").click()
        get_id(self, "com.unicocloud.smarthome:id/more_system_setting").click()
        get_id(self, "com.unicocloud.smarthome:id/lly_update").click()
        t = get_id(self, "com.unicocloud.smarthome:id/tv_no_update").text
        self.assertEqual(t, "已经是最新版本", "测试失败")
        cutScreenShot(self, "test_updata")

    # AP管理
    def test_ap(self):
        sleep(5)
        get_xpath(self, "//*[@text='我的']").click()
        get_id(self, "com.unicocloud.smarthome:id/lly_router").click()
        get_id(self, "com.unicocloud.smarthome:id/llt_wireless_setting").click()
        get_id(self, "com.unicocloud.smarthome:id/led_state").click()
        if find_toast("msg timeout", self.driver):
            cutScreenShot(self, "ap指示灯开启失败")
            self.assertTrue(False)

    # 存储管理
    def test_storage(self):
        sleep(3)
        try:
            get_xpath(self, "//*[@text='我的']").click()
            storage = round(int(getACstorage()) / 1024)
            get_id(self, "com.unicocloud.smarthome:id/rl_route_room").click()
            text = get_id(self, "com.unicocloud.smarthome:id/tv_available_space").text
            self.assertEqual(round(text[0:-1]), storage, "剩余空间显示不正确")
        except:
            cutScreenShot(self, "存储异常截图")
            self.assertTrue(False)

