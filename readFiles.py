# read the csv files with python using CSV library
# simple python program to read the csv data
# working code
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




# ##read the csv files with python using pandas library
# working code
# import pandas as pd
# data = pd.read_csv("mockData.csv")
# print(data)
# print(type(data)) #<class 'pandas.core.frame.DataFrame'>


