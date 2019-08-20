#coding = utf-8
import unittest,time
from Common.loginfo import Log
from Common import gesture_manipulation,base_page
from Common import driver_configure
from appium.webdriver.common import mobileby

class SearchUrl(unittest.TestCase):

    log = Log()
    @classmethod
    def setUpClass(self):
        dconfigur = driver_configure.driver_configure()
        self.driver = dconfigur.get_driver()
        self.GM = gesture_manipulation.gesture_mainpulation()
        self.YD = base_page.Base_page(self.driver)
    def test01_searchUrl(self):
        """在搜索框输入网址，验证是否能跳转到相关网页"""
        by = mobileby.MobileBy()
        self.YD.findElement(by.ID,"com.vivo.browser:id/search_text").click()
        self.YD.Send_keys("www.baidu.com",by.ID,"com.vivo.browser:id/edit")
        self.YD.findElement(by.ID, "com.vivo.browser:id/search_btn").click()
        time.sleep(2)
        # 向下划动
        for i in range(0,3):
            self.GM.swipe_down(self.driver)
        # 向上划动
        for i in range(0,3):
            self.GM.swipe_up(self.driver)
        assert "百度" in self.driver.page_source
        self.log.info("成功跳转到搜索的网页并能正常划动页面")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()


