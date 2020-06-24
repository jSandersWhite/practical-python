# pcost.py
#
# Exercise 1.27
import csv
import sys
import report
import stock

def portfolioCost(filert):
    '''
    Reads file at filert and calculates total cost of stock formatted to two decimals
    '''
    portfolio = report.readPortfolio(filert)
    
    return portfolio.total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit('Usage: %s portfile' % args[0])
    print('Total cost', portfolioCost(argv[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv)