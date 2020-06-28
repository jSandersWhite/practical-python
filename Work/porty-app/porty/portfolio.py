from . import stock
from . import fileparse

class Portfolio:
    def __init__(self):
        self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()

    def __len__(self):
        return len(self.holdings)

    def __getitem__(self, index):
        return self.holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self.holdings)

    @property
    def total_cost(self):
        return sum(s.cost for s in self.holdings)

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self.holdings.append(holding)

    def tabulateShares(self):
        from collections import Counter
        totalShares = Counter()
        for s in self._holdings:
            totalShares[s.name] += s.shares
        return totalShares

    @classmethod
    def fromCsv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parseCsv(lines, select=['name', 'shares', 'price'], types=[str,int,float], **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self