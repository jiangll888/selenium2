import logging
import os,time
import threading

class LogRecord:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def __new__(cls, *args, **kwargs):
        _instance_lock = threading.Lock()
        if not hasattr(cls,"_instance"):
            with _instance_lock:
                if not hasattr(cls,"_instance"):
                    cls._instance = super().__new__(cls)
        return cls._instance

    def log_record(self,obj=None):
        if obj:
            case_name = obj._testMethodName
        else:
            case_name = "case_log"
        dirname = os.path.join(os.path.dirname(os.path.abspath(__file__)),"logs\\" + time.strftime("%Y-%m-%d") + "\\")
        isExists = os.path.exists(dirname)
        # 判断结果
        if not isExists:
            os.makedirs(dirname)
        filename = os.path.join(dirname + case_name + "  " + time.strftime("%H_%M_%S")+".log")
        self.appender = logging.FileHandler(filename,mode="a",encoding="utf-8")
        self.appender.setLevel(logging.INFO)
        fomatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(lineno)d  %(levelname)s --> %(message)s")
        self.appender.setFormatter(fomatter)
        self.logger.addHandler(self.appender)
        return self.logger

    def close(self):
        self.appender.close()
        self.logger.removeHandler(self.appender)


if __name__ == "__main__":
    # l = LogRecord()
    # l.log_record()
    # filename = os.path.join(os.getcwd(), "logs\\" + time.strftime("%Y-%m-%d %H_%M_%S") + ".log")
    # print(filename)
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs\\" + time.strftime("%Y-%m-%d %H_%M_%S") + ".log")
    print(filename)
    print(os.path.abspath(__file__))
    print(__file__)
    print(__package__)