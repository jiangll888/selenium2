from base.browser_engine import BrowserEngine
import unittest
import ddt
import os,time
import multiprocessing
from case.run_main import RunMain
from util.opera_db import OperationDB
import HTMLTestRunner
from page.login_page import LoginPage
from config import settings
from pic.opera_pics import OperaPics

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

    # @ddt.unpack
    # def setUp(self,*args,**kwargs):
    #     print(kwargs)

    @ddt.unpack
    def test(self,*args,**kwargs):
        global r
        r = RunMain(kwargs)
        #res = r.run_main(self.driver,parames)
        self.res = r.run_main(self.driver)
        if self.res != None:
            self.assertTrue(self.res)

    def tearDown(self):
        if r.is_run and self.res:
            r.post_act(self.driver)   #数据清理操作
        OperaPics().save_pic_main(self)

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        op_db.close()
        r.send_result_mail()

def get_suite(i):
    global parames
    if i == 0:
        parames = "chrome"
    elif i == 1:
        parames = "firefox"
    else:
        parames = "edge"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    #unittest.TextTestRunner().run(suite)
    filename = "../report/" + parames + "/" + time.strftime("%Y-%m-%d %H-%M-%S") + ".html"
    with open(filename, "wb") as fp:
        HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="selenium_test_report", description="test").run(
            suite)

if __name__ == "__main__":
    unittest.main()
    # for i in range(3):
    #     p = multiprocessing.Process(target=get_suite,args=[i,])
    #     p.start()
    #r.send_result_mail()
