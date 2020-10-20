#coding:utf-8
from selenium import webdriver
import unittest,time

# https://www.cnblogs.com/linbao/p/7601316.html
# def login(driver, username, password):#此处的driver是个形参,如果不在此处定义就不可以使用
# 　　 #点击登录的操作
#     driver.find_element_by_link_text("登录").click()
#     #输入用户名
#     driver.find_element_by_css_selector("#input1").send_keys(username)
#     time.sleep(2)
#     #输入密码
#     driver.find_element_by_css_selector("#input2").send_keys(password)
#     # 点击登录
#     time.sleep(2)
#     driver.find_element_by_id("signin").click()

class Test_Log(unittest.TestCase):
    def setUp(self):
        url="https://www.cnblogs.com/"
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('lang=zh_CN.UTF-8')
        self.option.add_argument('User-Agent:"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"')
        self.driver = webdriver.Chrome(chrome_options=self.option)
        self.driver.get(url)
    def test_1log(self):    #登录失败
        #调用login函数,并向它传参
        # login(driver=self.driver,username=u"uname",password=u"falsepwd")
        time.sleep(2)
        #实际结果
        actual_result=self.driver.find_element_by_css_selector("#tip_btn").text
        print("实际结果为:"+actual_result)
        time.sleep(2)
        #预期结果
        expected_result = u"用户名或密码错误\n\n联系 contact@cnblogs.com"
        print("预期结果为:" + expected_result)
        time.sleep(2)
        self.assertEqual(actual_result,expected_result,msg="实际结果(%s)与预期结果(%s)不一致"%(actual_result,expected_result))

    def test_2log(self):    #登录成功
        #调用login函数,并向它传参
        login(driver=self.driver,username=u"uname",password=u"truepwd")

        time.sleep(2)
        #实际结果
        actual_result=self.driver.find_element_by_css_selector("#span_userinfo>a:nth-child(1)").text
        print("实际结果为:"+actual_result)
        #预期结果
        expected_result="女林"
        print("预期结果为:"+expected_result)
        self.assertEqual(actual_result,expected_result,msg="实际结果(%s)与预期结果(%s)不一致"%(actual_result,expected_result))

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()