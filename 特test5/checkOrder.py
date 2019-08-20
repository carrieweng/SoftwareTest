#coding = utf-8
from appium import webdriver
import time
from selenium.webdriver.common.by import By
desired_caps = {
             "platformName":"Android",
             "deviceName":"4ca76a92",
             "platformVersion":"8.1",
             "appPackage":"com.sicherdata.youduo.andriod",
             "appActivity":".MainActivity",
             "automationName": "uiautomator2",
             # "unicodeKeyboard":"True",
             # "resetKeyboard":"True",
             "noReset":"True",
             #"appWaitActivity":"com.sicherdata.youduo.andriod/.MainActivity",
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
time.sleep(3)

driver.find_elements_by_android_uiautomator("new UiSelector().text(\"查看流水\")")[0].click()
time.sleep(1)
text2 = driver.find_elements_by_android_uiautomator("new UiSelector().text(\"查看流水\")")[0].text
assert "查看流水" in text2
#上下划动流水页面
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
#向下划动
driver.swipe(x/2,y*3/4,x/2,y/4,1000)
#向上划动
driver.swipe(x/2, y/4, x/2, y*3/4, 1000)
time.sleep(2)
#选择收银员进行筛选
driver.find_element_by_xpath("//android.widget.TextView[@text='收银员']").click()
time.sleep(1)

driver.quit()
