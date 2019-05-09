from base.base_page import BasePage
from base.get_element import GetElement
from selenium import webdriver
from config import settings
import threading

class LoginPage(BasePage):
    url = settings.BASE_URL
    _instance_lock = threading.Lock()

    def __init__(self,driver):
        super(LoginPage,self).__init__(driver,self.url)
        self.get_ele = GetElement(driver)

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

    def login(self,*args,**kwargs):
        self.open()
        self.click_element(self.get_login_type_element())
        self.send_msg(self.get_username_element(),kwargs["username"])
        self.send_msg(self.get_password_element(),kwargs["password"])
        self.click_element(self.get_login_btn_element())


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=settings.CHROME_PATH)
    l = LoginPage(driver,settings.URL)
    l.login("jiangliulin@163.com","baimaonv08340822")
