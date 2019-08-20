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
time.sleep(5)

driver.find_elements_by_class_name("android.widget.EditText")[0].clear()
driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys("19965871654")
driver.find_elements_by_class_name("android.widget.EditText")[1].clear()
driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys("123456")
time.sleep(2)

driver.find_elements_by_class_name("android.widget.TextView")[2].click()
time.sleep(1)
text1 = driver.find_elements_by_android_uiautomator("new UiSelector().text(\"登录成功\")")[0].text
if text1 == "登录成功":
    print("success")
else:
    print("failed")
time.sleep(3)

#开始收款
driver.find_elements_by_class_name("android.widget.TextView")[1].click()
time.sleep(2)
driver.find_elements_by_class_name("android.widget.EditText")[0].click()
driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys("0.01")
time.sleep(1)
driver.find_elements_by_android_uiautomator("new UiSelector().text(\"开始收款\")")[0].click()
time.sleep(2)
#返回到首页
driver.press_keycode(4)
time.sleep(1)
driver.press_keycode(4)
time.sleep(2)

# #查看流水
# driver.find_elements_by_class_name("android.widget.TextView")[3].click()
# time.sleep(1)


driver.quit()