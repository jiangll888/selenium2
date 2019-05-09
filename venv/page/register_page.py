from base.base_page import BasePage
from config import settings
from base.get_element import GetElement
from selenium import webdriver

class RegisterPage(BasePage):
    url = settings.BASE_URL

    def __init__(self,driver):
        self.driver = driver
        self.get_e = GetElement(self.driver)
        super(RegisterPage,self).__init__(self.driver,self.url)

    # def get_value(self):
    #     self.url = settings.URL

    def get_email_element(self):
        email_element = self.get_e.get_element("email","register_element")
        return email_element

    def get_username_element(self):
        return self.get_e.get_element("username","register_element")

    def get_password_element(self):
        return self.get_e.get_element("password","register_element")

    def get_code_image_element(self):
        return self.get_e.get_element("code_image","register_element")

    def get_code_text_element(self):
        return self.get_e.get_element("code_text","register_element")

    def get_register_btn_element(self):
        return self.get_e.get_element("register_btn","register_element")

    def get_email_error_element(self):
        return self.get_e.get_element("email_error","register_element")

    def get_email_error_text(self):
        try:
            text = self.get_email_error_element().text
            return text
        except:
            return None

    def register(self,*args,**kwargs):
        self.open()
        self.send_msg(self.get_email_element(),kwargs["email"])
        self.send_msg(self.get_username_element(),kwargs["username"])
        self.send_msg(self.get_password_element(),kwargs["password"])
        self.send_msg(self.get_code_text_element(),kwargs["code"])
        self.click_element(self.get_register_btn_element())

    def assert_result(self,expect,expect_method):
        func = getattr(self,expect_method)
        res = func()
        if expect == res:
            return True
        else:
            return False

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r"E:\tools\selenium\chromedriver_win32\chromedriver.exe")
    r = RegisterPage(driver)
    r.register("jia","tese1111","123456","12345")
    print(r.get_email_error_text())
    # a = "RegisterPage"
    # b = eval(a)
    # c = b(driver)
