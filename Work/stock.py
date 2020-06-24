class Stock:
    __slots__ = ('name', '_shares', 'price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
        
    @property
    def shares(self):
        return self._shares

    @property
    def cost(self):
        return self.shares * self.price

    @shares.setter
    def shares(self, val):
        if not isinstance(val, int):
            raise TypeError('Expected int')
        self._shares = val

    def sell(self, qty):
        if qty > self.shares:
            print('You do not have that many shares of', self.name, 'to sell')
        else:
            self.shares = self.shares - qty

class NewStock(Stock):
    def yow(self):
        print('Yow!')