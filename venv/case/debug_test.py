import unittest
import os,ddt
from base.browser_engine import BrowserEngine
import time
import HTMLTestRunner
from pic.opera_pics import OperaPics
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pic.opera_pics import OperaPics
from selenium.common.exceptions import TimeoutException
from util.read_ini import ReadIni
# @ddt.ddt
# class Test(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = BrowserEngine("chrome").start_browser()
#
#     @ddt.data({"a":1})
#
#     @ddt.unpack
#     def test(self,a):
#         try:
#             print(rr)
#         except:
#             raise TimeoutError
#             #raise NameError
#             print(1111111111111)
#
#     # def test01(self):
#     #     print(222222222222222)
#
#     def tearDown(self):
#         OperaPics().save_pic(self)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
class Test:


    def __init__(self, filename=None):
        self.driver = BrowserEngine("chrome").start_browser()
        self.op_pic = OperaPics()
        self.filename = filename
        self.r = ReadIni(self.filename)
        self.op_pic = OperaPics()

    def get_element_key(self, key, section=None):
        element_key = self.r.get_value(key, section)
        if element_key:
            element_key_list = element_key.split(">")
        else:
            element_key_list = None
            print("配置文件中未取到该元素")
        return element_key_list

    def test(self):
        self.driver = BrowserEngine("chrome").start_browser()
        OperaPics().save_pic(self)

    # def wait_element_disappear(self,key,timeout=10,poll=0.5):
    #     wait = WebDriverWait(self.driver,timeout,poll)
    #     try:
    #         key_tuple = (By.ID, key)
    #         res = wait.until_not(EC.visibility_of_element_located(key_tuple))
    #         return res
    #     except TimeoutException as e:
    #         print("元素：{} 还未消失".format(key))
    #         print(e)
    #         self.op_pic.save_pic(self)
    #         return False
    def wait_element_disappear(self,key,section=None,timeout=5,poll=0.5):
        key_list = self.get_element_key(key, section)
        wait = WebDriverWait(self.driver,timeout,poll)
        try:
            if key_list[0] == 'id':
                key_tuple = (By.ID, key_list[1])
            elif key_list[0] == 'name':
                key_tuple = (By.NAME, key_list[1])
            else:
                key_tuple = (By.XPATH, key_list[1])
            res = wait.until_not(EC.visibility_of_element_located(key_tuple))
            return res
        except TimeoutException as e:
            print("元素：{} 还未消失".format(key_list[1]))
            self.op_pic.save_pic(self)
            return False

if __name__ == "__main__":
    # unittest.main()
    t= Test()
    t.driver.get("https://www.baidu.com")
    t.wait_element_disappear("BAIDU_SU","BAIDU_ELEMENT")

