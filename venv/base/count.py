from config import settings
from util.opera_db import OperationDB

class Count:
    def __init__(self):
        self.op_db = OperationDB()
        self.chrome_result = self.get_chrome_result()
        self.firefox_result = self.get_firefox_result()
        self.edge_result = self.get_edge_result()

    def get_chrome_result(self):
        chrome_result = self.op_db.search_all("select " + settings.CHROME_RESULT + " from `ui_cases`;")
        res = [r[settings.CHROME_RESULT] for r in chrome_result]
        return res

    def get_firefox_result(self):
        firefox_result = self.op_db.search_all("select " + settings.FIREFOX_RESULT + " from `ui_cases`;")
        res = [r[settings.FIREFOX_RESULT] for r in firefox_result]
        return res

    def get_edge_result(self):
        edge_result = self.op_db.search_all("select " + settings.EDGE_RESULT + " from `ui_cases`;")
        res = [r[settings.EDGE_RESULT] for r in edge_result]
        return res

    def get_result(self):
        chrome_pass = chrome_fail = firefox_pass = firefox_fail = edge_pass = edge_fail = 0
        for i in self.chrome_result:
            if  i == "pass":
                chrome_pass += 1
            elif i == "fail":
                chrome_fail +=1
        for j in self.firefox_result:
            if j == "pass":
                firefox_pass += 1
            elif j == "fail":
                firefox_fail +=1
        for k in self.edge_result:
            if k == "pass":
                edge_pass += 1
            elif k == "fail":
                edge_fail +=1
        return  str(chrome_pass),str(chrome_fail),str(firefox_pass),str(firefox_fail),str(edge_pass),str(edge_fail)


if __name__ == "__main__":
    d = Count()
    r = d.get_result()
    print(r)
