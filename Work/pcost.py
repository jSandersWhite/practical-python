# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolioCost(filert):
    '''
    Reads file at filert and calculates total cost of stock formatted to two decimals
    '''
    total = 0.0

    with open(filert, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            try:
                total = total + int(row[1]) * float(row[2])
            except ValueError:
                print('Invalid value on line', row)


    return round(total, 2)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

cost = portfolioCost(filename)
print('Total cost', cost)