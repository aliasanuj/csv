# import csv
#
# header = ["name","city","salary"]
# data = [["anuj", "patna", 10000]]
#
# with open("sample01.csv", mode='w', newline="") as filename:
#     writer = csv.writer(filename)
#     writer.writerow(header)
#
#
#


import csv

with open('profiles2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    row_list = [
        ["name", "age", "country"],
        ["Oladele Damilola", "40", "Nigeria"],
        ["Alina Hricko", "23" "Ukraine"],
        ["Isabel Walter", "50" "United Kingdom"],
    ]

    writer.writerow(row_list)
