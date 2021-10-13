import unittest
from customer import Customer
from coins import Quarter, Dime, Nickel, Penny
from cans import Cola, OrangeSoda, RootBeer


class TestGetWalletCoin(unittest.TestCase):
    """Tests for customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin(Quarter())
        self.assertEqual(returned_coin.value, .25)
        
    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin(Dime())
        self.assertEqual(returned_coin.value, .10)

    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin(Nickel())
        self.assertEqual(returned_coin.value, .05)

    def test_can_return_penny(self):
        """Pass in 'Penny', method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin(Penny())
        self.assertEqual(returned_coin.value, .01)
        
    def test_can_not_return_string(self):
        """Pass in 'Ponny', method should return a none value"""
        returned_coin = self.customer.get_wallet_coin('Ponny')
        self.assertEqual(returned_coin, None)

class TestAddCoinsToWallet(unittest.TestCase):

    def setUp(self):
        self.customer = Customer()

    def test_add_coins_to_wallet_increase_value(self):
        """Test for customers add coins to wallet method to see if it increases list value"""
        
        coins_list= [Penny(), Nickel(), Quarter(), Dime()]

        # for coin in coins_list:
        #     self.customer.wallet.money.append(coin)
        self.customer.add_coins_to_wallet(coins_list)
        self.assertEqual(len(self.customer.wallet.money), 91)    
    
    
    def test_add_coins_to_wallet_value_stays_same(self):
        """Test for customers add coins to wallet method to see if empty list doens't change the value"""

        coins_list= []  

        for coin in coins_list:
         self.customer.wallet.money.append(coin)
         self.assertEqual(len(self.customer.wallet.money), 89)    

    
class TestAddCanToBackpack(unittest.TestCase):    

    def setUp(self):
        self.customer = Customer()
    
    def test_add_can_to_backpack_cola(self):
        """Pass in a'Cola', method should return a  purchased_cans instance"""
        self.customer.add_can_to_backpack(Cola())
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)            
    
    def test_add_can_to_backpack_orangesoda(self):
        """Pass in a'OrangeSoda', method should return a  purchased_cans instance"""
        self.customer.add_can_to_backpack(OrangeSoda())
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
      
    def test_add_can_to_backpack_rootbeer(self):
        """Pass in a'RootBeer', method should return a  purchased_cans instance"""
        self.customer.add_can_to_backpack(RootBeer())
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
    

if __name__ == '__main__': 
    unittest.main()