import logging
import os,time
class LogRecord:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def log_record(self):
        #self.appender = logging.StreamHandler()
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),"logs\\"+time.strftime("%Y-%m-%d %H_%M_%S")+".log")
        self.appender = logging.FileHandler(filename,mode="a")
        self.appender.setLevel(logging.INFO)
        fomatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(lineno)d  %(levelname)s --> %(message)s")
        self.appender.setFormatter(fomatter)
        self.logger.addHandler(self.appender)
        #self.logger.info("test")
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