# report.py
#
# Exercise 2.4
from . import fileparse
from .stock import Stock
from . import tableformat
from .portfolio import Portfolio

def readPortfolio(filename, **options):
    with open(filename) as file:
        portfolio = Portfolio.fromCsv(file, **options)

    return portfolio

def readPrices(filename):
    with open(filename) as file:
        prices = fileparse.parseCsv(file, types=[str, float], hasHeaders=False)

    return dict(prices)

def calculate(portfolio, prices):
    currentTotal = 0.0
    initialTotal = 0.0

    for stock in portfolio:
        currentTotal += stock.shares * prices[stock.name]
        initialTotal += stock.shares * stock.price

    return {
        'value': round(currentTotal, 2),
        'cost': round(initialTotal, 2),
        'gain': round(currentTotal - initialTotal, 2)
    }

def makeReport(reportdata, formatter):
    '''
    Print a formatted table from a list of (name, shares, price, change) tuples
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def makeReportData(portfolio, prices):
    '''
    Format and calculate report data into tuple
    '''
    list = []
    for stock in portfolio:
        if stock.name in prices:
            diff = prices[stock.name] - stock.price
            holding = (stock.name, stock.shares, prices[stock.name], diff)
            list.append(holding)

    return list

        
def portfolioReport(portfolioFile, priceFile, fmt = 'txt'):
    '''
    Make a stock report given portfolio and price data files
    '''
    portfolio = readPortfolio(portfolioFile)
    prices = readPrices(priceFile)
    report = makeReportData(portfolio, prices)

    formatter = tableformat.createFormatter(fmt)
    makeReport(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolioReport(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)