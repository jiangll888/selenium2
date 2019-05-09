import xlrd

class OperaExcel:
    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = "../config/case.xls"
        self.data = self.read_data()
        self.sheet_data = self.read_sheet()

    def read_data(self):
        data = xlrd.open_workbook(self.filename)
        return data

    def read_sheet(self,sheet=None):
        if sheet == None:
            sheet = 0
        sheet_data = self.data.sheet_by_index(sheet)
        return sheet_data

    def row_count(self):
        return self.sheet_data.nrows

    def row_data(self,row):
        row_value =  self.sheet_data.row_values(row)
        for i in range(len(row_value)):
            if isinstance(row_value[i],float):
                row_value[i] = str(int(row_value[i]))
        return row_value

if __name__ == "__main__":
    op = OperaExcel()
    print(op.row_count())
    print(op.row_data(1))