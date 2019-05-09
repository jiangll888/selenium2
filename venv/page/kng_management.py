from base.base_page import BasePage
from config import settings
from base.get_element import GetElement
import time
import threading

class KngManagement(BasePage):
    url = settings.KNG_URL
    _instance_lock = threading.Lock()

    def __init__(self,driver):
        super(KngManagement,self).__init__(driver,self.url)
        self.get_ele = GetElement(driver)

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

    def check_file(self,file_type):
        if file_type == "pic":
            #在播放页查看图片是否正常
            return self.check_jpg_file()
        elif file_type == "doc":
            return self.check_doc_file()
        elif file_type == "video":
            return self.check_video_file()
        else:
            return self.check_audio_file()

    def get_first_edit_btn_element(self):
        return self.get_ele.get_element("first_file_edit_btn","kng_element")

    def get_first_delete_btn_element(self):
        return self.get_ele.get_element("first_file_delete_btn","kng_element")

    def get_loading_status(self):
        return self.get_ele.get_element("loading_status","kng_element")

    def enter_upload_page(self):
        self.open()
        self.click_element(self.get_share_kng_btn_element())
        self.switch_window()

    def delete_file(self):
        self.move_to_target(self.get_first_edit_btn_element())
        self.click_element(self.get_first_delete_btn_element())
        al = self.switch_alert()
        al.accept()
        self.get_ele.wait_element_disappear("loading_status","kng_element")