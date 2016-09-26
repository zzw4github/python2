import xlrd

data = xlrd.open_workbook("e:/python.xls")

table = data.sheets()[0]

row = table.row_values(0)
for data in row:
    print data


