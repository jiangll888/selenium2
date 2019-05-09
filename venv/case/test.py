from page.register_page import RegisterPage
from base.browser_engine import BrowserEngine
import unittest
import ddt
from config.config_data import ConfigData
from base.assert_result import assert_result
import os,time
from log.log_record import LogRecord
import multiprocessing

c = ConfigData()
data = c.get_data_for_excel()

@ddt.ddt
class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserEngine(parames).start_browser()
        cls.rp = RegisterPage(cls.driver)
        cls.log = LogRecord()
        cls.logger = cls.log.log_record()

    @ddt.data(*data)

    @ddt.unpack
    def test(self,*args):
        self.rp.register(*args)
        self.expect = args[4]
        self.expect_method = args[5]

    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                self.logger.info("测试")
                case_name = self._testMethodName
                filename = os.path.join(os.path.dirname(os.getcwd()),"pic\\"+case_name+".png")
                self.driver.save_screenshot(filename)
        res = self.rp.assert_result(self.expect,self.expect_method)
        self.assertTrue(res)

    @classmethod
    def tearDownClass(cls):
        cls.log.close()
        cls.driver.quit()

def get_suite(i):
    global parames
    if i == 0:
        parames = "chrome"
    elif i == 1:
        parames = "firefox"
    else:
        parames = "edge"
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite1)

if __name__ == "__main__":
    # unittest.main()
    for i in range(3):
        p = multiprocessing.Process(target=get_suite,args=[i,])
        p.start()

