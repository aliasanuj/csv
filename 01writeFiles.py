'''to create a new csv file using python
working'''

# import csv
# # Define the headers
# headers = ['Name', 'Age', 'Country']
# # Define the data to be inserted
# data = [
#     [25, 'USA'],
#     ['Bob', 30,],
#     ['Charlie']
# ]
# # Open the CSV file in write mode
# with open('data.csv', mode='w', newline='') as file:
#     # Create a CSV writer object
#     print("file is ",file,"type is",type(file))
#     writer = csv.writer(file)
#     print("writer is ",writer ,"type is ",type(writer))
#     # Write the headers to the CSV file
#     writer.writerow(headers)
#     print("writer is ",writer ,"type is ",type(writer))
#     # Write the data to the CSV file
#     writer.writerows(data)
#     print("writer is ", writer, "type is ", type(writer))



'''checking for practise
working
creating a new csv file with new name along with dummy data'''

# import csv
# header = ["qqq","qqq","qqq"]
# data = [[" " ,"ddd"," "],["qq"],["qq"," ","rr"]]
# with open("filename.csv", mode='w') as file:
#     objectFile = csv.writer(file)
#     objectFile.writerow(header)
#     objectFile.writerows(data)



'''code for creating multiple sheets in xlsx using pyython
working'''

# import pandas as pd
# import re
# df1 = pd.DataFrame({'Data': ['arter', 'berger', 'cretre', 'd45yt45']})
# print(type(df1))
# df2 = pd.DataFrame({'Data': [1, 25, 35454, 4545]})
# df3 = pd.DataFrame({'Data': [1.15454, 1.25, 1.34353, 1.46545]})
# writer = pd.ExcelWriter(r'C:\Git\csv\filename.xlsx', engine='xlsxwriter')
# df1.to_excel(writer, sheet_name='Sheeta')
# df2.to_excel(writer, sheet_name='Sheetb')
# df3.to_excel(writer, sheet_name='Sheetc')
# writer._save()
#



'''clean code for creating multiple sheets in xlsx using pyython'''

# import the python pandas package
# import pandas as pd
# import re
# # create  data_frame1 by creating a dictionary
# # in which values are stored as list
# data_frame1 = pd.DataFrame({'Fruits': ['Appple', 'Banana', 'Mango',
#                                        'Dragon Fruit', 'Musk melon', 'grapes'],
#                             'Sales in kg': [20, 30, 15, 10, 50, 40]})
# # create  data_frame2 by creating a dictionary
# # in which values are stored as list
# data_frame2 = pd.DataFrame({'Vegetables': ['tomato', 'Onion', 'ladies finger',
#                                            'beans', 'bedroot', 'carrot'],
#                             'Sales in kg': [200, 310, 115, 110, 55, 45]})
# # create  data_frame3 by creating a dictionary
# # in which values are stored as list
# data_frame3 = pd.DataFrame({'Baked Items': ['Cakes', 'biscuits', 'muffins',
#                                             'Rusk', 'puffs', 'cupcakes'],
#                             'Sales in kg': [120, 130, 159, 310, 150, 140]})
# print(data_frame1)
# print(data_frame2)
# print(data_frame3)
# # create a excel writer object
# with pd.ExcelWriter(r"filename01.xlsx") as writer:
#     # use to_excel function and specify the sheet_name and index
#     # to store the dataframe in specified sheet
#     data_frame1.to_excel(writer, sheet_name="Fruits", index=False)
#     data_frame2.to_excel(writer, sheet_name="Vegetables", index=False)
#     data_frame3.to_excel(writer, sheet_name="Baked Items", index=False)

