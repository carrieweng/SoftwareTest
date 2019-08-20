# coding:utf-8
__author__ = 'Carrie'

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Base_page:
    def __init__(self,driver):
        self.driver = driver

    def findElement(self,*loc):
        '''重写find_element方法，显式等待'''
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            raise e

    def findElements(self, *loc):
        '''重写find_element方法，显式等待'''
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except NoSuchElementException as e:
            raise e

    def Send_keys(self, value,*loc):
        try:
            self.findElement(*loc).clear()
            self.findElement(*loc).send_keys(value)
        except NoSuchElementException as e:
            raise e

    def ElementsSend_keys(self, value,*loc):
        try:
            self.findElements(*loc).clear()
            self.findElements(*loc).send_keys(value)
        except NoSuchElementException as e:
            raise e

    def tab1(self,driver,a1,b1):
        c1 = a1 / 1080
        d1 = b1 / 2154
        # 获取当前手机屏幕大小X,Y
        X = driver.get_window_size()['width']
        Y = driver.get_window_size()['height']
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        driver.tap([(a1 * X,c1 * Y)])
        return driver.tap([(c1 * X,d1 * Y)])

    def quit(self):
        return self.driver.quit()