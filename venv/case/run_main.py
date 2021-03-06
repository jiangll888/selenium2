from config.config_data import DataConfig
from case import *
import json
import time
import threading
from util.send_mail import SendMail
from config import settings
from log.log_record import LogRecord

class RunMain:
    _instance_lock = threading.Lock()

    def __init__(self,data,logger):
        self.data = data
        self.get_field()
        self.logger = logger

    def __new__(cls, *args, **kwargs):
        '''
        实现单例模式
        :param args:
        :param kwargs:
        :return:
        '''
        if not hasattr(cls,"_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super().__new__(cls)
        return cls._instance

    def get_field(self):
        dc = DataConfig(self.data)
        self.case_id = dc.get_case_id()
        self.pre_action = dc.get_pre_action()
        self.action = dc.get_action()
        self.is_run = dc.get_is_run()
        self.request_data = dc.get_params()
        self.post_action = dc.get_post_action()
        self.expect = dc.get_expext()
        self.expect_method = dc.get_expect_method()
        self.expect_method_params = dc.get_expect_method_params()

    def run_main(self,driver,browser_type="chrome"):
        if self.is_run:
            action_list = self.action.split(">")
            page_class = eval(action_list[0])
            ob = page_class(driver,self.logger)
            func = getattr(ob, action_list[1])
            res = func(browser_type,**self.request_data)
            expect_method_list = self.expect_method.split(">")  #预期结果先不执行了
            page_class1 = eval(expect_method_list[0])
            ob1 = page_class1(driver,self.logger)
            r = ob1.assert_result(self.expect,expect_method_list[1],self.expect_method_params)
            self.write_res(r,browser_type)
            return r

    def write_res(self,res,browser_type):
        dc = DataConfig(self.data)
        if browser_type == "chrome":
            sql = settings.UPDATE_CHROME_RESULT_SQL
        elif browser_type == "firefox":
            sql = settings.UPDATE_FIREFOX_RESULT_SQL
        else:
            sql = settings.UPDATE_EDGE_RESULT_SQL

        if res:
            para = ("pass", self.case_id)
        else:
            para = ("fail", self.case_id)
        dc.write_result(sql,para)

    def post_act(self,driver):
        '''
        数据清理操作
        :return:
        '''
        if self.post_action:
            post_action_list = self.post_action.split(">")
            page_class = eval(post_action_list[0])
            ob = page_class(driver,self.logger)
            func = getattr(ob, post_action_list[1])
            func()




if __name__ == "__main__":
    r = RunMain(1)

