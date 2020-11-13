import pandas

df_xlsx = pandas.read_excel('test_data.xlsx')
print(df_xlsx.head(5))

df = pandas.read_excel('csv_data.xlsx')
print(df.head(5))

