import unittest
import TestCases.common.Initialize as initialize
from TestCases.common.InitLogin import init_login


class TestLogin(unittest.TestCase):
    driver = None

    # setUpClass方法在类初始化时仅调用一次
    @classmethod
    def setUpClass(cls):
        cls.driver = initialize.setUp()

        print("----------------setUpClass-------------")

    # setUp方法在case执行前调用（多条case被调用多次）
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # Initialize.setUp(self)
        # self.driver.implicitly_wait(5)

        print("----------------setup-------------")

    def tearDown(self):
        print("-------------teardown------------------")
        # Initialize.tearDown(self)

    def test_login(self):
        init_login(self)


