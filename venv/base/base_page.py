from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time,os
from pic.opera_pics import OperaPics

class BasePage:
    def __init__(self,driver,logger,url=None):
        self.driver = driver
        self.url = url
        self.action = ActionChains(self.driver)
        self.op_pic = OperaPics()
        self.logger = logger

    def open(self):
        self.logger.info("打开"+self.url)
        self.driver.get(self.url)
        self.maxsize_window()

    def refresh(self):
        self.logger.info("刷新页面")
        self.driver.refresh()

    def close(self):
        self.logger.info("关闭当前页面")
        self.driver.close()

    def get_title(self):
        self.logger.info("获取当前页面title")
        return self.driver.title

    def get_url(self):
        self.logger.info("关闭当前页面url")
        return self.driver.current_url

    def maxsize_window(self):
        self.logger.info("窗口最大化")
        self.driver.maximize_window()

    def send_msg(self,element,message):
        try:
            element.clear()
            element.send_keys(message)
            self.logger.info("在{}元素处输入{}成功".format(str(element),message))
        except:
             self.logger.error("在{}元素处输入{}失败".format(str(element),message) )
             self.op_pic.save_pic(self)

    def click_element(self,element):
        try:
            element.click()
            self.logger.info("在{}元素处点击成功".format(str(element)))
        except:
            self.logger.error("在{}元素处点击失败".format(str(element)))
            self.op_pic.save_pic(self)

    # def save_pic(self):
    #     self.driver.save_screenshot()

    def switch_iframe(self,element=None):
        try:
            if element == None:
                self.driver.switch_to.default_content()
            else:
                #self.wait.until(EC.visibility_of(element))
                self.driver.switch_to.frame(element)
            self.logger.info("切换iframe成功")
        except:
            self.logger.error("切换iframe失败")
            self.op_pic.save_pic(self)

    def switch_window(self,handle_num=-1):
        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[handle_num])
            self.logger.info("切换window成功")
        except:
            self.logger.error("切换window失败")
            self.op_pic.save_pic(self)

    def switch_alert(self):
        try:
            al = self.driver.switch_to.alert
            self.logger.info("切换alert成功")
            return al
        except:
            self.logger.error("切换alert失败")
            self.op_pic.save_pic(self)

    def drag_and_drop_element(self,source,target):
        try:
            self.action.drag_and_drop(source,target).perform()
            self.logger.info("拖拽{}到{}成功".format(str(source),str(target)))
        except:
            self.logger.error("拖拽{}到{}失败".format(str(source),str(target)))
            self.op_pic.save_pic(self)

    def move_to_target(self,element):
        try:
            self.action.move_to_element(element).perform()
            self.logger.info("在{}处鼠标悬停成功".format(str(element)))
        except:
            self.logger.error("在{}处鼠标悬停失败".format(str(element)))
            self.op_pic.save_pic(self)

    def execute_autoit_script(self,cmd):
        try:
            os.system(cmd)
            self.logger.info("{} 脚本执行成功".format(cmd))
        except:
            self.logger.error("{} 脚本执行失败".format(cmd))
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

