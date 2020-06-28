class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def rot(self, rowdata):
        '''
        emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plaintext format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowData):
        for d in rowData:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowData):
        print(','.join(rowData))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML
    '''
    def headings(self, headers):
        head = ''
        for header in headers:
            head = head + '<th>' + header + '</th>'
        head = '<tr>' + head + '</tr>'
        print(head)

    def row(self, rowData):
        row = ''
        for item in rowData:
            data = self.htmlDataWrap(item)
            row += data

        print('<tr>' + row + '</tr>')

    def htmlDataWrap(self, item):
        formattedString = ''
        formattedString += '<td>' + item + '</td>'
        
        return formattedString

class FormatError(Exception):
    pass


def createFormatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError('Unknown format %s' % fmt)
            
def printTable(data, columns, formatter):
    formatter.headings(columns)
    for item in data:
        row = [ str(getattr(item, name)) for name in columns ]
        formatter.row(row)


