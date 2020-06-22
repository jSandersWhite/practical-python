# pcost.py
#
# Exercise 1.27
import csv
import sys
import report

def portfolioCost(filert):
    '''
    Reads file at filert and calculates total cost of stock formatted to two decimals
    '''
    total = 0.0
    portfolio = report.readPortfolio(filert)
    for row in portfolio:
        try:
            total = total + row['shares'] * row['price']
        except ValueError:
            print('Invalid value on line', row)


    return round(total, 2)

def main(argv):
    if len(argv) != 2:
        raise SystemExit('Usage: %s portfile' % args[0])
    print('Total cost', portfolioCost(argv[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv)