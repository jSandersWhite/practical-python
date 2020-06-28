from .follow import follow
import csv
from . import report
from .tableformat import createFormatter

def parseStockData(lines, indices, headers, types, names):
    rows = csv.reader(lines)
    rows = ([row[index] for index in indices] for row in rows)
    rows = ([func(val) for func, val in zip(types,row)] for row in rows)
    rows = (dict(zip(headers, row)) for row in rows)
    rows = (row for row in rows if row['Name'] in names)
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.readPortfolio(portfile)
    lines = follow(logfile)
    headers = ['Name', 'Price', 'Change']
    rows = parseStockData(lines, [0, 1, 4], headers, [str, float, float], names = portfolio)
    formatter = createFormatter(fmt)
    formatter.headings(headers)
    for row in rows:
        formatter.row([ row['Name'], f"{row['Price']:0.2f}", f"{row['Change']:0.2f}"] )

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile logfile format' % args[0])
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
    