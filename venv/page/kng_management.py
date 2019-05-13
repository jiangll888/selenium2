from base.base_page import BasePage
from config import settings
from base.get_element import GetElement
import time
import threading
from base.browser_engine import BrowserEngine
from log.log_record import LogRecord

class KngManagement(BasePage):
    url = settings.KNG_URL

    def __init__(self,driver,logger):
        self.logger = logger
        super(KngManagement,self).__init__(driver,self.logger,self.url)
        self.get_ele = GetElement(driver,self.logger)

    def get_share_kng_btn_element(self):
        return self.get_ele.get_element("share_kng_btn","kng_element")

    def get_jpg_file_element(self):
        return self.get_ele.get_element("jpg_file_element","kng_element")

    def get_doc_file_element(self):
        return self.get_ele.get_element("doc_file_element","kng_element")

    def get_video_file_element(self):
        return self.get_ele.get_element("video_file_element","kng_element")

    def get_audio_file_element(self):
        return self.get_ele.get_element("audio_file_element","kng_element")

    def get_doc_file_element(self):
        return self.get_ele.get_element("doc_file_element","kng_element")

    def get_video_file_element(self):
        return self.get_ele.get_element("video_file_element","kng_element")

    def get_audio_file_element(self):
        return self.get_ele.get_element("audio_file_element","kng_element")

    def get_scorm_file_element(self):
        return self.get_ele.get_element("scorm_file_element","kng_element")

    def get_html_file_element(self):
        return self.get_ele.get_element("html_file_element","kng_element")

    def check_jpg_file(self):
        if self.get_jpg_file_element():
            return True
        else:
            return False

    def check_doc_file(self):
        if self.get_doc_file_element():
            return True
        else:
            return False

    def check_video_file(self):
        if self.get_video_file_element():
            return True
        else:
            return False

    def check_audio_file(self):
        if self.get_audio_file_element():
            return True
        else:
            return False

    def check_scorm_file(self):
        if self.get_scorm_file_element():
            return True
        else:
            return False

    def check_html_file(self):
        if self.get_html_file_element():
            return True
        else:
            return False

    def check_file(self,file_type):
        if file_type == "pic":
            #在播放页查看图片是否正常
            return self.check_jpg_file()
        elif file_type == "doc":
            return self.check_doc_file()
        elif file_type == "video":
            return self.check_video_file()
        elif file_type == "audio":
            return self.check_audio_file()
        elif file_type == "scorm":
            return self.check_scorm_file()
        else:
            return self.check_html_file()
        # check_file_dict = {"pic":self.check_jpg_file,
        #                    "doc":self.check_doc_file,
        #                    "video":self.check_video_file,
        #                    "audio":self.check_audio_file(),
        #                    "scorm":self.check_scorm_file(),
        #                    "html":self.check_html_file()}
        # func = check_file_dict.get(file_type,default="类型错误")
        # if func != "类型错误":
        #     return func()
        # else:
        #     self.logger.warning("传入的文件类型错误，无法检测其是否在知识列表里")


    def get_first_edit_btn_element(self):
        return self.get_ele.get_element("first_file_edit_btn","kng_element")

    def get_first_delete_btn_element(self):
        return self.get_ele.get_element("first_file_delete_btn","kng_element")

    def get_loading_status(self):
        return self.get_ele.get_element("loading_status","kng_element")

    def get_scorm_upload_btn(self):
        return self.get_ele.get_element("upload_scorm_btn","kng_element")

    def get_html_upload_btn(self):
        return self.get_ele.get_element("upload_html_btn","kng_element")

    def enter_upload_page(self):
        self.open()
        self.click_element(self.get_share_kng_btn_element())
        self.switch_window()

    def enter_upload_scorm_page(self):
        self.open()
        self.move_to_target(self.get_share_kng_btn_element())
        self.click_element(self.get_scorm_upload_btn())
        self.switch_window()

    def enter_upload_html_page(self):
        self.open()
        self.move_to_target(self.get_share_kng_btn_element())
        self.click_element(self.get_html_upload_btn())
        self.switch_window()

    def delete_file(self):
        self.move_to_target(self.get_first_edit_btn_element())
        self.click_element(self.get_first_delete_btn_element())
        al = self.switch_alert()
        al and al.accept()
        self.get_ele.wait_element_disappear("loading_status","kng_element")

if __name__ == "__main__":
    driver = BrowserEngine("chrome").start_browser()
    log = LogRecord()
    logger = log.log_record()
