import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(BaseTestCase):


    def test_baidu_search(self):
        #测试方法必须要以test开头
        #声明HomePage对象
        home_page = HomePage(self.driver)
        # home_page.open_url("http://www.baidu.com")
        #调用首页搜索功能
        home_page.search("selenium")

        #
        # time.sleep(2)
        # assert "selenium" in self.driver.title



if __name__ == '__main__':
    unittest.main()
