'''append the data into csv files.
working code'''

# import csv
# # open the CSV file in append mode
# with open('mockData.csv', 'a', newline='') as file:
#     # create a CSV writer object
#     writer = csv.writer(file)
#
#     # write a new row to the CSV file
#     writer.writerow(['John', 'Doe', '25'])


'''used to append data in xlsx with different pre existing sheets and also it will create new sheet
working code'''

# from openpyxl import load_workbook
# # load the existing workbook
# workbook = load_workbook('mockData.xlsx')
# # create a new worksheet
# # worksheet = workbook.create_sheet('data') ##it will create new sheet and add the data
# worksheet = workbook['data'] ##it will ask the sheetname an after provided, it will append the data in the bottom
# # append data to the new worksheet
# worksheet.append(['Jane', 'Doe', 30])
# # save the changes to the workbook
# workbook.save('mockData.xlsx')


"""In general, you cannot insert data in the middle of a
CSV file directly, because CSV files are designed to be
read and written sequentially. However, you can simulate
inserting data in the middle of a CSV file by creating a new
CSV file and copying the data from the original CSV file to
the new file, with the new data inserted at the desired location.
Here's an example of how to do it:"""
"""this is Chat GPT suggestion and code
working code"""

# import csv
# # open the original CSV file and the new CSV file
# with open('mockData.csv', 'r') as infile, open('new_mockData.csv', 'w', newline='') as outfile:
#     # create a CSV reader and writer objects
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)
#
#     # loop through the rows in the original CSV file
#     for i, row in enumerate(reader):
#         # write the row to the new CSV file
#         writer.writerow(row)
#
#         # insert new data after the third row
#         if i == 2:
#             new_row = ['John', 'Doe', '25']
#             writer.writerow(new_row)



