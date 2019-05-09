from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time,os
from pic.opera_pics import OperaPics

class BasePage:
    def __init__(self,driver,url=None):
        self.driver = driver
        self.url = url
        self.action = ActionChains(self.driver)
        self.op_pic = OperaPics()

    def open(self):
        self.driver.get(self.url)
        self.maxsize_window()

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def maxsize_window(self):
        self.driver.maximize_window()

    def send_msg(self,element,message):
        try:
            element.clear()
            element.send_keys(message)
        except:
             print("元素输入失败")
             self.op_pic.save_pic(self)

    def click_element(self,element):
        try:
            element.click()
        except:
            print("元素点击不到")
            self.op_pic.save_pic(self)

    def save_pic(self):
        self.driver.save_screenshot()

    def switch_iframe(self,element=None):
        try:
            if element == None:
                self.driver.switch_to.default_content()
            else:
                #self.wait.until(EC.visibility_of(element))
                self.driver.switch_to.frame(element)
        except:
            print("切换iframe失败")
            self.op_pic.save_pic(self)

    def switch_window(self,handle_num=-1):
        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[handle_num])
        except:
            print("切换window失败")
            self.op_pic.save_pic(self)

    def switch_alert(self):
        try:
            al = self.driver.switch_to.alert
            return al
        except:
            print("切换alert失败")
            self.op_pic.save_pic(self)

    def drag_and_drop_element(self,source,target):
        try:
            self.action.drag_and_drop(source,target).perform()
        except:
            print("拖拽失败")
            self.op_pic.save_pic(self)

    def move_to_target(self,element):
        try:
            self.action.move_to_element(element).perform()
        except:
            print("鼠标悬停失败")
            self.op_pic.save_pic(self)

    def execute_autoit_script(self,cmd):
        try:
            os.system(cmd)
        except:
            print("cmd脚本执行失败")
            self.op_pic.save_pic(self)
            
    def assert_result(self,expect,expect_method,expect_method_params=None):
        func = getattr(self,expect_method)
        if expect_method_params:
            res = func(**expect_method_params)
        else:
            res = func()
        if expect == res:
            return True
        else:
            return False

