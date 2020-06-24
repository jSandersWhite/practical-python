from follow import follow
import csv
import report
from tableformat import createFormatter

def parseStockData(lines, columns, headers, types):
    rows = csv.reader(lines)
    rows = selectColumns(rows, columns)
    rows = convertTypes(rows, types)
    rows = makeDicts(rows, headers)
    return rows

def selectColumns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def makeDicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def convertTypes(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types,row)]

def filterSymbols(rows, names):
    for row in rows:
        if row['Name'] in names:
            yield row

def ticker(portfile, logfile, fmt):
    portfolio = report.readPortfolio(portfile)
    lines = follow(logfile)
    headers = ['Name', 'Price', 'Change']
    rows = parseStockData(lines, [0, 1, 4], headers, [str, float, float])
    rows = filterSymbols(rows, portfolio)    
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
    