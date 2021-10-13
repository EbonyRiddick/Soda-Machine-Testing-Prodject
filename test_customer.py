import unittest
from customer import Customer

class TestGetWalletCoin(unittest.TestCase):
    """Tests for customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, .25)
        
    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.value, .10)

    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, .05)

    def test_can_return_penny(self):
        """Pass in 'Penny', method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.value, .01)
        
    def test_can_not_return_string(self):
        """Pass in 'Ponny', method should return a none value"""
        returned_coin = self.customer.get_wallet_coin('Ponny')
        self.assertEqual(returned_coin, None)
        
    def test_add_can_to_backpack_cola(self):
        """Pass in a'Cola', method should return a  purchased_cans instance"""
        self.customer.backpack.purchased_cans.append('Cola')
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)

    def test_add_can_to_backpack_orangesoda(self):
        """Pass in a'OrangeSoda', method should return a  purchased_cans instance"""
        self.customer.backpack.purchased_cans.append('OrangeSoda')
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
      
    def test_add_can_to_backpack_rootbeer(self):
        """Pass in a'RootBeer', method should return a  purchased_cans instance"""
        self.customer.backpack.purchased_cans.append('RootBeer')
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
    

if __name__ == '__main__':
    unittest.main()