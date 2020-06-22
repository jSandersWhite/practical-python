# fileparse.py
#
# Exercise 3.3
import csv

def parseCsv(file, select = None, types = None, hasHeaders = True, silenceErrors = True, delimiter=','):
    '''
    Parce a CSV file into a list of records
    '''
    rows = csv.reader(file, delimiter=delimiter)

    if select and not hasHeaders:
        raise RuntimeError("Select argument requires column headers")

    headers = None
    # read the file headers
    if hasHeaders:
        headers = next(rows)

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    rowCount = 1
    for row in rows:
        try:
            if not row: # Skip empty rows
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            rowCount += 1
        except ValueError as e:
            print('Row', rowCount, ': Couldn\'t convert', row)
            print('Row', rowCount, 'Reason', e)

        if headers:
            record = dict(zip(headers, row))
        else:
            record = row
        records.append(record)

    return records