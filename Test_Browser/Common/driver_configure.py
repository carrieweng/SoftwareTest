# coding:utf-8
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class driver_configure():
     def get_driver(self):
        try:
            desired_caps = {"platformName": "Android",
                            "deviceName": "4ca76a92",
                            "platformVersion": "8.1",
                            "appPackage": "com.vivo.browser",
                            "appActivity": ".MainActivity",
                            "automationName": "uiautomator2",
                            # "unicodeKeyboard":"True",
                            # "resetKeyboard":"True",
                            "noReset": "True"}
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(30)
            return self.driver
        except:
            print("启动异常")



