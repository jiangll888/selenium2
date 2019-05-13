from page.kng_management import KngManagement
from base.get_element import GetElement
import time
import os
from config import  settings

class UploadScormPage(KngManagement):

    def __init__(self,driver,logger):
        self.logger = logger
        super().__init__(driver,logger)
        self.get_ele = GetElement(driver,logger)

    def get_upload_html_file_btn(self):
        return self.get_ele.get_element("upload_html_btn","upload_html_element")

    def get_course_name(self):
        return self.get_ele.get_element("course_name","upload_html_element")

    def get_submit_btn(self):
        return self.get_ele.get_element("submit_btn","upload_html_element")

    def get_upload_status(self):
        return self.get_ele.get_element("upload_status","upload_html_element")

    def upload_html(self):
        self.enter_upload_html_page()
        upload_html_element = self.get_upload_html_file_btn()
        time.sleep(2)
        self.click_element(upload_html_element)
        cmd = settings.AUTOIT3_SCRIPT_PATH + " " + args[0] + " " + kwargs["filename"]
        self.execute_autoit_script(cmd)
        self.send_msg(self.get_course_name(),settings.HTML_COURSE_NAME)
        if self.get_upload_status():
            time.sleep(1)
            self.click_element(self.get_submit_btn())
            self.switch_window(0)

