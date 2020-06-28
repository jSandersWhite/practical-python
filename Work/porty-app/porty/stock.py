from .typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, qty):
        if qty > self.shares:
            print('You do not have that many shares of', self.name, 'to sell')
        else:
            self.shares = self.shares - qty

class NewStock(Stock):
    def yow(self):
        print('Yow!')