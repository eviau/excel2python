import pyexcel 

sheet = pyexcel.get_sheet(file_name="test_data.xlsx")
print(sheet)

sheet2 = pyexcel.get_sheet(file_name="csv_data.xlsx")
print(sheet2)


