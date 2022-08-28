from HTMLTestRunner import HTMLTestRunner
from test_case import Test_Case 
import unittest

class Test(unittest.TestCase):

    def test_suit(self):
        mysuit = unittest.TestSuite()

        case_list = ['test_001','test_002','test_003']
        for case in case_list:
            mysuit.addTest(Test_Case(case))
        with open('report.html','wb') as f:
            HTMLTestRunner(f,title='第一个测试报告',description='我要自学网网页登录',verbosity=2).run(mysuit)

if __name__ == '__main__':
    unittest.main()