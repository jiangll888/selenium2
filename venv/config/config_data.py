from config import settings
from util.opera_db import OperationDB
import json

class DataConfig:

    def __init__(self,data):
        self.db_data = data
        self.op_db = OperationDB()

    def get_case_id(self):
        return self.db_data and self.db_data[settings.CASE_ID]

    def get_case_name(self):
        return self.db_data and self.db_data[settings.CASE_NAME]

    def get_pre_action(self):
        return self.db_data and self.db_data[settings.PRE_ACTION]

    def get_action(self):
        return self.db_data and self.db_data[settings.ACTION]

    def get_post_action(self):
        return self.db_data and self.db_data[settings.POST_ACTION]

    def get_params(self):
        return self.db_data and self.db_data[settings.PARAMS] and json.loads(self.db_data[settings.PARAMS])

    def get_is_run(self):
        return self.db_data and self.db_data[settings.IS_RUN]

    def get_expext(self):
        return self.db_data and self.db_data[settings.EXPECT]

    def get_expect_method(self):
        return self.db_data and self.db_data[settings.EXPECT_METHOD]

    def get_expect_method_params(self):
        return self.db_data and self.db_data[settings.EXPECT_METHOD_PARAMS] and json.loads(self.db_data[settings.EXPECT_METHOD_PARAMS])

    def write_result(self,sql,param):
        self.op_db.sql_DML(sql,param)

if __name__ == "__main__":
    db = OperationDB(settings.DB_TYPE, settings.DB_USER, settings.DB_PASSWD, settings.DB_HOST, settings.DB_PORT,
                             settings.DB_NAME)
    sql = "select * from ui_cases where case_id=%s"
    pa = ("register_001",)
    data = db.search_one(sql,pa)
    d = DataConfig(data)
    r = d.get_edge_result()
    print(r)
    # sql1 = "update ui_cases set result=%s where case_id=%s"
    # para1 = ("pass","register_001")
    # d.write_result(sql1,para1)


