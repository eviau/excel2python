import xlrd

book = xlrd.open_workbook('test_data.xlsx')
print(book)

book2 = xlrd.open_workbook('csv_data.xlsx')
print(book2)