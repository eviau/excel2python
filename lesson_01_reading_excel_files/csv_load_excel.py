import csv

with open('csv_data.xlsx') as excel_file:
    xcl_rdr = csv.reader(excel_file, dialect='excel')
    print(xcl_rdr)
    for row in xcl_rdr:
        print(row)