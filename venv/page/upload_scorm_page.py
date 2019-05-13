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

    def get_upload_scorm_file_btn(self):
        return self.get_ele.get_element("upload_scorm_btn","upload_scorm_element")

    def get_course_provider_no_btn(self):
        return self.get_ele.get_element("course_provider_no","upload_scorm_element")

    def get_course_provider_name_btn(self):
        return self.get_ele.get_element("course_provider_name","upload_scorm_element")

    def get_submit_btn(self):
        return self.get_ele.get_element("submit_btn","upload_scorm_element")

    def get_upload_status(self):
        return self.get_ele.get_element("upload_status","upload_scorm_element")

    def upload_scorm(self,*args,**kwargs):
        self.enter_upload_scorm_page()
        upload_btn_element = self.get_upload_scorm_file_btn()
        time.sleep(2)
        self.click_element(upload_btn_element)
        cmd = settings.AUTOIT3_SCRIPT_PATH + " " + args[0] + " " + kwargs["filename"]
        self.execute_autoit_script(cmd)
        self.send_msg(self.get_course_provider_no_btn(),settings.SCORM_COURSE_PROVIDER_NO)
        self.send_msg(self.get_course_provider_name_btn(),settings.SCORM_COURSE_PROVIDER_NAME)
        if self.get_upload_status():
            time.sleep(1)
            self.click_element(self.get_submit_btn())
            self.switch_window(0)
