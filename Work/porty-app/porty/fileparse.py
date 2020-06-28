# fileparse.py
#
# Exercise 3.3
import csv
import logging
log = logging.getLogger(__name__)
logging.basicConfig(
    filename = 'app.log',
    filemode = 'w',
    level = logging.WARNING
)

def parseCsv(file, select = None, types = None, hasHeaders = True, silenceErrors = True, delimiter=','):
    '''
    Parce a CSV file into a list of records
    '''
    if select and not hasHeaders:
        raise RuntimeError("Select argument requires column headers")

    rows = csv.reader(file, delimiter=delimiter)

    # read the file headers
    headers = next(rows) if hasHeaders else []

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row: # Skip empty rows
            continue
        if select:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silenceErrors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        if headers:
            record = dict(zip(headers, row))
        else:
            record = row
        records.append(record)

    return records