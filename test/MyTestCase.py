import base64
import unittest
import time
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/wuxiaolei/dev/chromedriver')

    def testcaptureScreen(self):
        url="https://data.yupaopao.com/#/ypp/dashboard/index"
        password=base64.b64decode("QWRtaW4xMjM=").decode("utf-8")
        print(password)
        self.driver.get(url)
        #输入用户名
        self.driver.find_element_by_css_selector("#username").send_keys("wuxiaolei")
        # self.time.sleep(2)
        #输入密码
        self.driver.find_element_by_css_selector("#password").send_keys(password)
        # 点击登录
        self.driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        try:
            result=self.driver.get_screenshot_as_file(r"./photo1.png")
            print(result)
        except IOError as e:
            print(e)

if __name__ == "__main__":
    unittest.main()