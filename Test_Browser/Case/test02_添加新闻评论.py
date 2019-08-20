#coding = utf-8
import unittest,time
from Common.loginfo import Log
from Common import gesture_manipulation,base_page
from Common import driver_configure
from appium.webdriver.common import mobileby

class AddComment(unittest.TestCase):

    log = Log()
    @classmethod
    def setUpClass(self):
        dconfigur = driver_configure.driver_configure()
        self.driver = dconfigur.get_driver()
        self.GM = gesture_manipulation.gesture_mainpulation()
        self.YD = base_page.Base_page(self.driver)
    def test01_addComment(self):
        """在搜索框输入网址，验证是否能跳转到相关网页"""
        by = mobileby.MobileBy()
        self.YD.findElements(by.CLASS_NAME,"android.widget.ImageView")[2].click()
        time.sleep(4)
        self.YD.findElement(by.ID,"com.vivo.browser:id/input").click()
        self.YD.Send_keys("aaa",by.ID,"com.vivo.browser:id/content")
        self.YD.findElement(by.ID,"com.vivo.browser:id/submit").click()
        time.sleep(1)
        assert "成功" in self.driver.page_source
        self.log.info("成功添加新闻评论")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()


