from base.base_page import BasePage
from base.get_element import GetElement
from selenium import webdriver
from config import settings
import threading
from base.captcha import HandleCaptcha
from log.log_record import LogRecord

class LoginPage(BasePage):
    url = settings.BASE_URL
    _instance_lock = threading.Lock()

    def __init__(self,driver,logger):
        self.logger = logger
        super(LoginPage,self).__init__(driver,self.logger,self.url)
        self.get_ele = GetElement(driver,self.logger)

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

    def get_username_element(self):
        return self.get_ele.get_element("username","login_element")

    def get_password_element(self):
        return self.get_ele.get_element("password","login_element")

    def get_login_btn_element(self):
        return self.get_ele.get_element("login_btn","login_element")

    def get_login_type_element(self):
        return self.get_ele.get_element("login_type","login_element")

    def get_sms_login_type_element(self):
        return self.get_ele.get_element("sms_login_type","login_element")

    def get_phone_no_element(self):
        return self.get_ele.get_element("phone_no_text","login_element")

    def get_code_text_element(self):
        return self.get_ele.get_element("code_text","login_element")

    def get_code_img_element(self):
        return self.get_ele.get_element("code_img","login_element")

    def get_dcode_text_element(self):
        return self.get_ele.get_element("dcode_text","login_element")

    def get_dcode_btn_element(self):
        return self.get_ele.get_element("dcode_btn","login_element")

    def get_sms_login_btn_element(self):
        return self.get_ele.get_element("sms_login_btn","login_element")

    def login(self,*args,**kwargs):
        self.open()
        self.click_element(self.get_login_type_element())
        self.send_msg(self.get_username_element(),kwargs["username"])
        self.send_msg(self.get_password_element(),kwargs["password"])
        self.click_element(self.get_login_btn_element())

    def login_sms(self,*args,**kwargs):
        self.open()
        self.click_element(self.get_sms_login_type_element())
        self.send_msg(self.get_phone_no_element(),kwargs["phone_no"])
        #点击验证码输入框
        code_text_element = self.get_code_text_element()
        self.logger.info("点击验证码输入框（点击之后验证码会发生变化，所以要先点击后截图）")
        self.click_element(code_text_element)
        #识别图片验证码
        self.logger.info("识别图片验证码")
        capt = HandleCaptcha(self.driver,self.logger)
        code = capt.handle_captcha(self.get_code_img_element())
        #输入图片验证码
        self.logger.info("输入图片验证码")
        self.send_msg(code_text_element,code)
        #点击获取动态码
        self.logger.info("点击获取手机动态验证码")
        self.click_element(self.get_dcode_btn_element())
        #需要写一个方法去短信平台拿到验证码
        #输入动态验证码
        #self.logger.info("输入手机动态验证码")
        #self.send_msg(self.get_code_text_element(),"")
        #点击登录
        #self.click_element(self.get_sms_login_btn_element())

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=settings.CHROME_PATH)
    log = LogRecord()
    logger = log.log_record()
    l = LoginPage(driver,logger)
    l.login_sms(**{"phone_no":15995807141})
    #l.login("jiangliulin@163.com","baimaonv08340822")

