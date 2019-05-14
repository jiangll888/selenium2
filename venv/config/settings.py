import os
#URL = "http://www.5itest.cn/register"
BASE_URL = "http://jgtest.qida.yunxuetang.com.cn/login.htm"
KNG_URL = "http://jgtest.qida.yunxuetang.com.cn/kng/kngmgmt/kngknowledgemgmt.htm"

CHROME_PATH = r"E:\tools\selenium\chromedriver_win32\chromedriver.exe"
FIREFOX_PATH = r"E:\tools\selenium\geckodriver\geckodriver.exe"
EDGE_PATH = r"E:\tools\selenium\edge\MicrosoftWebDriver.exe"

CASE_ID = "case_id"
CASE_NAME = "case_name"
PRE_ACTION = "pre_action"
ACTION = "action"
PARAMS = "params"
POST_ACTION = "post_action"
IS_RUN = "is_run"
EXPECT = "expect"
EXPECT_METHOD = "expect_method"
EXPECT_METHOD_PARAMS = "expect_method_params"
CHROME_RESULT = "chrome_result"
FIREFOX_RESULT = "firefox_result"
EDGE_RESULT = "edge_result"


DB_TYPE = "mysql"
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PORT = 3306
DB_PASSWD = "122901"
DB_NAME = "testing"
TABLE_NAME = "`ui_cases`"

# AUTOIT3_SCRIPT_PATH = "D:\\atuoit3\\test\\yunxu11.exe"
AUTOIT3_SCRIPT_PATH = os.path.join(os.path.dirname(os.getcwd()),"util\\yunxu11.exe")
DOWNLOAD_PATH = r"C:\Users\夏君\Downloads"

TEST_CASE_SQL = "select * from {};".format(TABLE_NAME)
CLEAR_RESULT_SQL = "update {} set {}='',{}='',{}='';".format(TABLE_NAME,CHROME_RESULT,FIREFOX_RESULT,EDGE_RESULT)
UPDATE_CHROME_RESULT_SQL = "update {} set {}=%s where {}=%s;".format(TABLE_NAME,CHROME_RESULT,CASE_ID)
UPDATE_FIREFOX_RESULT_SQL = "update {} set {}=%s where {}=%s;".format(TABLE_NAME,FIREFOX_RESULT,CASE_ID)
UPDATE_EDGE_RESULT_SQL = "update {} set {}=%s where {}=%s;".format(TABLE_NAME,EDGE_RESULT,CASE_ID)
GET_CHROME_RESULT = "select {}  from {};".format(CHROME_RESULT,TABLE_NAME)
GET_FIREFOX_RESULT = "select {}  from {};".format(FIREFOX_RESULT,TABLE_NAME)
GET_EDGE_RESULT = "select {}  from {};".format(EDGE_RESULT,TABLE_NAME)

EMAIL_CONTENT = "本次自动化分别在Chrome浏览器、Firefox浏览器、Edge浏览器上执行了{}个测试用例。\n" \
                "其中在Chrome浏览器上运行成功{}个，在Chrome浏览器上运行失败{}个\n"\
                "在Firefox浏览器上运行成功{}个，在Firefox浏览器上运行失败{}个\n"\
                "在Edge浏览器上运行成功{}个，在Edge浏览器上运行失败{}个\n"\
                "测试报告地址:{}\n"\
                "可在数据库中查看运行结果，数据库类型：{}，数据库地址：{}，用户名：{}，密码：{}，"\
                "数据库库名：{}，数据库表名：{}"

EMAIL_SUB = "selenium自动化测试报告   {}"
EMAIL_RECEIVER = ["jiangliulin@163.com"]

SCORM_COURSE_PROVIDER_NO = "112233"
SCORM_COURSE_PROVIDER_NAME = "test_scorm"
HTML_COURSE_NAME = "html_5_7"

PIC_RATIO = 1.5
CODE_LOC = r"E:/code.png"


