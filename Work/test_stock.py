import unittest
import stock

class TestStock(unittest.TestCase):
    def createStock(self):
        return stock.Stock('GOOG', 100, 490.1)

    def test_create(self):
        s = self.createStock()
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = self.createStock()
        self.assertEqual(s.cost, (s.shares * s.price))

    def test_sell(self):
        s = self.createStock()
        shares = s.shares
        sub = 25
        s.sell(sub)
        self.assertEqual(s.shares, (shares - sub))

    def test_bad_shares(self):
        s = self.createStock()
        with self.assertRaises(TypeError):
            s.shares = '100'

if __name__ == '__main__':
    unittest.main()