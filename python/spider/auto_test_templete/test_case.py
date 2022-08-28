from login import Login
import unittest
from HTMLTestRunner import HTMLTestRunner

class Test_Case(unittest.TestCase):

    log = Login()
    def set_up(self):
        print('start')

    def tear_down(self):
        print("end")

    # 输入正确账号密码
    def test_001(self):
        self.log.login('19957061942',pwd='niu514647318')
        text = self.log.get_text('class_name','text-overflow')
        # 断言预期结果与实际结果一致
        self.assertEqual(text,'text-overflow')
        self.log.quit()

    def test_002(self):
        self.log.login('199', pwd='')
        # 预期登录信息
        text = self.log.get_text('id', 'pwd-error')
        self.assertEqual(text,'密码不能为空')
        log.quit()

    def test_003(self):
        self.log.login('199','niu')
        text = self.log.get_text('class_name', 'msgText')
        self.assertEqual(text,'登录失败，请检查登录信息是否有误')

if __name__ == '__main__':
    # 1
    # unittest.main()
    # 2
    # 实例套件，向套件中添加用例
    my_suit = unittest.TestSuite()
    test_cases = ['test_001','test_002','test_003']
    for case in test_cases:
        my_suit.addTest(Test_Case(case))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(my_suit)
    # 3 
    with open('report.html','wb') as f:
        HTMLTestRunner(f,title='第一个测试报告',description='我要自学网网页登录',verbosity=2).run(my_suit)



