import xlrd
from Library.config import Config
# from config import Config

class ReadExcel:

    def read_testdata(self, sheetname):

        wb = xlrd.open_workbook(Config.TEST_DATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []

        for row in rows:
            if columns == 1:
                data.append(row[0].value)
            else:

                values = ()
                for j in range(columns):
                    values += (row[j].value,)
                data.append(values)
        return data

    def read_locators(self, sheetname):
        wb = xlrd.open_workbook(Config.LOCATOR_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)

        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d
