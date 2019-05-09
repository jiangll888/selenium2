from base.base_page import BasePage
from config import settings
from base.get_element import GetElement
from page.kng_management import KngManagement
from page.show_page import ShowPage
import time

class UploadPage(KngManagement):
    url = settings.KNG_URL

    def __init__(self,driver):
        super(UploadPage,self).__init__(driver)
        self.get_ele = GetElement(driver)

    def get_upload_file_btn(self):
        return self.get_ele.get_element("upload_file_btn","upload_element")

    def get_continue_upload_btn(self):
        return self.get_ele.get_element("continue_upload_btn","upload_element")

    def get_submit_file_btn(self):
        return self.get_ele.get_element("submit_file_btn","upload_element")

    def get_upload_status(self):
        return self.get_ele.get_element("upload_status","upload_element",200)

    def upload_file(self,*args,**kwargs):
        self.enter_upload_page()
        upload_btn = self.get_upload_file_btn()
        time.sleep(2)
        self.click_element(upload_btn)
        #平均cmd语句，args[0]是指浏览器类型
        cmd = settings.AUTOIT3_SCRIPT_PATH + " " + args[0] + " "+ kwargs["filename"]
        self.execute_autoit_script(cmd)
        if self.get_upload_status():
            time.sleep(1)
            self.click_element(self.get_submit_file_btn())
            self.switch_window(0)
            if self.check_file(kwargs["file_type"]):
                s = ShowPage(self.driver)
                if s.check_encode_status(kwargs["file_type"]):
                    s.delete_download_file(**kwargs)
                    s.download()
                    self.close()
                    self.switch_window(0)



