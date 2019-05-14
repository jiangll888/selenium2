import os,time,sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(),"..\\Lib\\site-packages")))
from base.browser_engine import BrowserEngine
import unittest
import ddt
import multiprocessing
from case.run_main import RunMain
from util.opera_db import OperationDB
import HTMLTestRunner
from page.login_page import LoginPage
from config import settings
from pic.opera_pics import OperaPics
from log.log_record import LogRecord
from BeautifulReport import BeautifulReport

op_db = OperationDB()
data = op_db.search_all(settings.TEST_CASE_SQL)


@ddt.ddt
class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #清除以前的测试结果
        op_db.sql_DML(settings.CLEAR_RESULT_SQL)
        #cls.driver = BrowserEngine(parames).start_browser()
        cls.driver = BrowserEngine("chrome").start_browser()
        #lo = LoginPage(cls.driver)
        #lo.login(**{"username":"admin","password":11223


    @ddt.data(*data)

    @ddt.unpack
    # @unittest.skipIf(**data["is_run"] == 0,"不执行测试")
    def test(self,*args,**kwargs):
        self.log = LogRecord()
        self.logger = self.log.log_record(self)
        global r
        r = RunMain(kwargs,self.logger)
        #res = r.run_main(self.driver,parames)
        self.res = r.run_main(self.driver)
        if self.res != None:
            self.assertTrue(self.res)

    def tearDown(self):
        if r.is_run and self.res:
            r.post_act(self.driver)   #数据清理操作
        OperaPics().save_pic_main(self)
        self.log.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        op_db.close()

def get_suite(i):
    global parames
    if i == 0:
        parames = "chrome"
    elif i == 1:
        parames = "firefox"
    else:
        parames = "edge"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    filename = "../report/" + parames + "/" + time.strftime("%Y-%m-%d %H-%M-%S") + ".html"
    with open(filename, "wb") as fp:
        HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="selenium_test_report", description="test").run(
            suite)

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    filename = time.strftime("%Y-%m-%d %H-%M-%S")
    parames = "chrome"
    BeautifulReport(suite).report(description="发布测试",filename=filename,log_path="../report/" + parames)
    # # for i in range(3):
    #     p = multiprocessing.Process(target=get_suite,args=[i,])
    #     p.start()
    #r.send_result_mail()
