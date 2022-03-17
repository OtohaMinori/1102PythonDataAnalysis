'''
Date:2022.03.17
Name:幽霊Ｓ☄
SID:B10813180
Title:Ex.4
'''
'''
Q1.

'''

import csv
csvfile = "./data.csv"
with open(csvfile, 'r') as data:
    reader = csv.reader(data)
    for row in reader:
        print(','.join(row))
