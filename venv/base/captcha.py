from pic.opera_pics import OperaPics
from PIL import Image
from config import settings
import pytesseract
from ShowapiRequest import ShowapiRequest

from base.get_element import GetElement
from base.browser_engine import BrowserEngine
from log.log_record import LogRecord

class HandleCaptcha:
    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def handle_captcha(self,code_element):
        #整个页面截图
        filename = OperaPics().save_pic(self)
        #从中切出验证码的图片
        self.save_code_img(filename,code_element)
        #识别图片中的内容
        text = self.distinguish()
        return text

    # 从中切出验证码的图片
    def save_code_img(self,filename,code_element):
        loc = code_element.location
        left = loc['x']
        top = loc['y']
        right = left + code_element.size['width']
        bottom = top + code_element.size['height']
        im = Image.open(filename)
        img = im.crop((settings.PIC_RATIO*left,settings.PIC_RATIO*top,
                       settings.PIC_RATIO*right,settings.PIC_RATIO*bottom))
        img.save(settings.CODE_LOC)

    def distinguish_with_pytesseract(self):
        im = Image.open(settings.CODE_LOC)
        text = pytesseract.image_to_string(im)
        return text

    def distinguish(self):
        r = ShowapiRequest("http://route.showapi.com/184-4", "94789", "6de63c760b684ad1a928d0158cfaef95")
        r.addBodyPara("typeId", "34")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", settings.CODE_LOC) #文件上传时设置
        res = r.post()
        return res.json()["showapi_res_body"]["Result"]


if __name__ == "__main__":
    driver = BrowserEngine("chrome").start_browser()
    log = LogRecord()
    logger = log.log_record()
    h = HandleCaptcha(driver,logger)
    driver.get("http://jgtest.qida.yunxuetang.com.cn/login.htm")
    get_ele = GetElement(driver, logger)
    get_ele.get_element("sms_login_type", "login_element").click()
    code = get_ele.get_element("code_img","login_element")
    h.handle_captcha(code)
    #print(h.distinguish())


