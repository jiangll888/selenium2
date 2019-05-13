import os,time
import threading

class OperaPics:

    def __new__(cls, *args, **kwargs):
        _instance_lock = threading.Lock()
        if not hasattr(cls,"_instance"):
            with _instance_lock:
                if not hasattr(cls,"_instance"):
                    cls._instance = super().__new__(cls)
        return cls._instance

    def save_pic_main(self,obj):
        for method_name,error in obj._outcome.errors:
            if error:
                self.save_pic(obj)

    def save_pic(self,obj):
        #case_name = obj._testMethodName
        timestamp = time.strftime("%Y_%m_%d")
        path = os.path.join(os.path.dirname(os.getcwd()), "pic\\pics\\" + timestamp + "\\")
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            os.makedirs(path)
        filename = os.path.join(path + time.strftime("%H_%M_%S") + ".png")
        try:
            obj.driver.save_screenshot(filename)
            obj.logger.info("截图成功，截图文件为: " + filename)
            return filename
        except:
            obj.logger.error("截图失败")