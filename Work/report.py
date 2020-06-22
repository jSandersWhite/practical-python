# report.py
#
# Exercise 2.4
import fileparse

def readPortfolio(filename):
    with open(filename) as file:
        portfolio = fileparse.parseCsv(file, types=[str, int, float])

    return portfolio

def readPrices(filename):
    with open(filename) as file:
        prices = fileparse.parseCsv(file, types=[str, float], hasHeaders=False)

    return dict(prices)

def calculate(portfolio, prices):
    currentTotal = 0.0
    initialTotal = 0.0

    for row in portfolio:
        currentTotal += row['shares'] * prices[row['name']]
        initialTotal += row['shares'] * row['price']

    return {
        'value': round(currentTotal, 2),
        'cost': round(initialTotal, 2),
        'gain': round(currentTotal - initialTotal, 2)
    }

def makeReport(portfolio, prices):
    list = []

    for row in portfolio:
        if row['name'] in prices:
            diff = prices[row['name']] - row['price']
            holding = (row['name'], row['shares'], prices[row['name']], diff)
            list.append(holding)
    
    headers = ('Name', 'Shares', 'Price', 'Change')
    separator = '---------- '
    print('%10s %10s %10s %10s' % headers)
    print(separator * 4)
    for name, shares, price, change in list:
        print(f'{name:>10s} {shares:>10d} {price:>9.2f} {change:>10.2f}')
        
def portfolioReport(file1, file2):
    portfolio = readPortfolio(file1)
    prices = readPrices(file2)
    makeReport(portfolio, prices)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolioReport(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)