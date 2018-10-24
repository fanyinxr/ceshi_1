from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from framework.browser_engine import BrowserEngine
import time


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # 测试的前提准备工作

        browser = BrowserEngine()
        self.driver = browser.open_browser()

        # self.driver = webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        # self.driver.get("http://www.baidu.com")


    def tearDown(self):
        #测试结束后的操作
        time.sleep(3)
        self.driver.quit()
