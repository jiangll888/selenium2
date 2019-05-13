from base.base_page import BasePage
from config import settings
from base.get_element import GetElement
from page.kng_management import KngManagement
import time,os
from util.opera_file import OperaFile

class ShowPage(KngManagement):
    url = settings.KNG_URL

    def __init__(self,driver,logger):
        self.logger = logger
        super(ShowPage,self).__init__(driver,self.logger)
        self.get_ele = GetElement(driver,self.logger)

    def get_pic_or_doc_show_element(self):
        return self.get_ele.get_element("pic_or_doc_show","show_element")

    def get_video_show_element(self):
        return self.get_ele.get_element("video_show","show_element")

    def get_audio_show_element(self):
        return self.get_ele.get_element("audio_show","show_element")

    def get_scorm_show_element(self):
        return self.get_ele.get_element("scorm_show","show_element")

    def get_html_show_element(self):
        return self.get_ele.get_element("html_show","show_element")

    def get_fresh_btn_element(self):
        return self.get_ele.get_element("fresh_btn","show_element")

    def get_download_element(self):
        return self.get_ele.get_element("download_btn","show_element")

    def download(self):
        ele = self.get_download_element()
        self.click_element(ele)

    def delete_download_file(self,*args,**kwargs):
        #如果本地已有文件，则删除
        OperaFile(kwargs["filename"],kwargs["file_type"],self.logger).delete_file()

    def check_download_status(self,*args,**kwargs):
        #这里之所以用上传文件路径，是因为上传路径是可以控制的，而下载路径可能随环境改变而变动（此处下载路径没地方设置）
        #下载路径拼接上传文件名称，则构成下载之后的文件名称
        op_file = OperaFile(kwargs["filename"],kwargs["file_type"],self.logger)
        for i in range(10):
            if op_file.check_file_status():
                return "true"
            else:
                time.sleep(10)
        return "false"

    def check_pic_encode_status(self):
        # 在列表页点击图片名称
        self.get_ele.wait_element_disappear("loading_status","kng_element")
        jpg_file_element = self.get_jpg_file_element()
        self.click_element(jpg_file_element)
        self.switch_window()
        ele = self.get_pic_or_doc_show_element()
        if ele:
            self.logger.info("图片转换成功")
            return True
        else:
            self.logger.error("图片转换失败")
            return False

    def check_doc_encode_status(self):
        self.get_ele.wait_element_disappear("loading_status", "kng_element")
        self.click_element(self.get_doc_file_element())
        self.switch_window()
        for i in range(10):
            if self.get_ele.wait_element_disappear("doc_encode_status", "show_element"):
                break
            else:
                #整个页面刷新，局部刷新按钮点击之后有bug
                self.refresh()
        ele = self.get_pic_or_doc_show_element()
        if ele:
            self.logger.info("文档转换成功")
            return True
        else:
            self.logger.error("文档转换失败")
            return False

    def check_video_encode_status(self):
        self.get_ele.wait_element_disappear("loading_status", "kng_element")
        self.click_element(self.get_video_file_element())
        self.switch_window()
        for i in range(20):
            if self.get_ele.wait_element_disappear("video_encode_status", "show_element"):
                break
            else:
                # 整个页面刷新，局部刷新按钮点击之后有bug
                self.refresh()
        ele = self.get_video_show_element()
        if ele:
            self.logger.info("视频转换成功")
            return True
        else:
            self.logger.error("视频转换失败")
            return False

    def check_audio_encode_status(self):
        self.get_ele.wait_element_disappear("loading_status", "kng_element")
        self.click_element(self.get_audio_file_element())
        self.switch_window()
        for i in range(20):
            if self.get_ele.wait_element_disappear("audio_encode_status", "show_element"):
                break
            else:
                # 整个页面刷新，局部刷新按钮点击之后有bug
                self.refresh()
        ele = self.get_audio_show_element()
        if ele:
            self.logger.info("音频转换成功")
            return True
        else:
            self.logger.error("音频转换失败")
            return False

    def check_scorm_encode_status(self):
        self.get_ele.wait_element_disappear("loading_status", "kng_element")
        self.click_element(self.get_scorm_file_element())
        self.switch_window()
        for i in range(20):
            if self.get_ele.wait_element_disappear("scorm_encode_status", "show_element"):
                break
            else:
                # 整个页面刷新，局部刷新按钮点击之后有bug
                self.refresh()
        ele = self.get_scorm_show_element()
        self.close()
        self.switch_window(0)
        if ele:
            self.logger.info("scorm转换成功")
            return "true"
        else:
            self.logger.error("scorm转换失败")
            return "false"

    def check_html_encode_status(self):
        self.get_ele.wait_element_disappear("loading_status", "kng_element")
        self.click_element(self.get_scorm_file_element())
        self.switch_window()
        for i in range(20):
            if self.get_ele.wait_element_disappear("html_encode_status", "show_element"):
                break
            else:
                # 整个页面刷新，局部刷新按钮点击之后有bug
                self.refresh()
        ele = self.get_html_show_element()
        self.close()
        self.switch_window(0)
        if ele:
            self.logger.info("html转换成功")
            return "true"
        else:
            self.logger.error("html转换失败")
            return "false"

    def check_encode_status(self,file_type):
        if file_type == "pic":
            #在播放页查看图片是否正常
            return self.check_pic_encode_status()
        elif file_type == "doc":
            return self.check_doc_encode_status()
        elif file_type == "video":
            return self.check_video_encode_status()
        elif file_type == "audio":
            return self.check_audio_encode_status()
        elif file_type == "scorm":
            return self.check_scorm_encode_status()
        else:
            return self.check_html_encode_status()
