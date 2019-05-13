from util.read_ini import ReadIni
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pic.opera_pics import OperaPics
from selenium.common.exceptions import TimeoutException

class GetElement:
    def __init__(self,driver,logger,filename=None):
        self.driver = driver
        self.filename = filename
        self.r = ReadIni(self.filename)
        self.op_pic = OperaPics()
        self.logger = logger

    def get_element_key(self,key,section=None):
        element_key = self.r.get_value(key,section)
        if element_key:
            element_key_list = element_key.split(">")
        else:
            element_key_list = None
            self.logger.error("配置文件中未取到该元素")
            #print("配置文件中未取到该元素")
        return element_key_list

    def get_element(self,key,section=None,timeout=50,poll=0.5):
        key_list = self.get_element_key(key,section)
        wait = WebDriverWait(self.driver,timeout,poll)
        try:
            if key_list[0] == 'id':
                key_tuple = (By.ID,key_list[1])
            elif key_list[0] == 'name':
                key_tuple = (By.NAME,key_list[1])
            else:
                key_tuple = (By.XPATH,key_list[1])
            element = wait.until(EC.visibility_of_element_located(key_tuple))
            self.logger.info("元素：{} 已找到,元素信息为{}".format(key_list[1],str(element)))
        except TimeoutException as e:
            self.logger.warning("元素：{} 未找到".format(key_list[1]))
            self.op_pic.save_pic(self)
            element = None
        return element

    def wait_element_disappear(self,key,section=None,timeout=50,poll=0.5):
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
            self.logger.info("元素：{} 已消失".format(key_list[1]))
            return res
        except TimeoutException as e:
            self.logger.warning("元素：{} 还未消失".format(key_list[1]))
            #print("元素：{} 还未消失".format(key_list[1]))
            self.op_pic.save_pic(self)
            return False

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r"E:\tools\selenium\chromedriver_win32\chromedriver.exe")
    driver.get("http://www.5itest.cn/register")
    time.sleep(2)
    g = GetElement(driver)
    print(g.get_element("username"))




