'''read the csv files with python using CSV library
simple python program to read the csv data
working code'''

# import csv
# # Open the CSV file
# with open(r'mockData.csv',encoding='utf-8', mode='r') as csv_file: #both can be there encoding and mode as well
#     csv_reader = csv.reader(csv_file)
#     print(csv_reader)
#     print(type(csv_reader)) # we can iterate the data using for loop and type will be LIST | <class '_csv.reader'>
#     # Iterate over each row in the CSV file
#     for row in csv_reader:
#         # Do something with the data
#         # print(row)
#         print(type(row))




'''read the csv files with python using pandas library
working code'''

# import pandas as pd
# data = pd.read_csv("mockData.csv")
# print(data)
# print(type(data)) #<class 'pandas.core.frame.DataFrame'>
#
#




'''read the csv files with python using pandas library with sheets data as well
this is working code'''

# import pandas as pd
# ### read the Excel file
# xlsx = pd.read_excel('mockData.xlsx', sheet_name=None)
# print("xlsx is",xlsx)
# print("xlsx type is",type(xlsx)) # xlsx type is <class 'dict'>
# print("keys is ",xlsx.keys()) ## display the sheet names
# print("values is ",xlsx.values()) # will give bith tables data
# print(type(xlsx.keys())) ###<class 'dict_keys'>
# print(type(xlsx.values())) ###<class 'dict_values'>
# ### display the data in each sheet
# for sheet_name, sheet_data in xlsx.items():
#     print(f"\n{sheet_name}\n{'this can be use as logs' * 3}")
#     print(sheet_data.head(5))
#     print(type(sheet_data.head()))






