__author__ = "VioLet"

from ddt import data, file_data, unpack, ddt
import unittest


@ddt
class DataTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(2, 3)
    def test_data(self, value):
        print(value)
        print("test")


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
