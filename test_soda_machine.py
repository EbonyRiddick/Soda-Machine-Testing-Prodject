import unittest
from soda_machine import SodaMachine
from coins import Quarter, Dime, Nickel, Penny

class TestFillRegister(unittest.TestCase):
    """"Test method for filling register list"""

    def setUp(self):
        self.soda_machine= SodaMachine()



    def test_fill_register(self):
        register_total= self.soda_machine.register

        self.assertEqual(len(register_total), 88)


class TestFillInventory(unittest.TestCase):
    """"Test method for filling inventory list"""

    def setUp(self):
        self.soda_machine= SodaMachine() 

    """"Test method for determining if inventory gets filled"""
    def test_fill_inventory(self):
        inventory_total= self.soda_machine.inventory

        self.assertEqual(len(inventory_total), 30)



class TestGetCoinFromRegister(unittest.TestCase):
    """"Test method for get coin from register"""

    def setUp(self):
        self.soda_machine= SodaMachine()

    def test_get_coin_from_register_quarter(self):
        """"Test method for checking if Quarter is returned from register"""
        money= self.soda_machine.get_coin_from_register('Quarter')       
        self.assertEqual(money.name , "Quarter")
      
    def test_get_coin_from_register_nickel(self):
        """"Test method for checking if Nickel is returned from register"""
        money= self.soda_machine.get_coin_from_register('Nickel')       
        self.assertEqual(money.name , "Nickel")

    def test_get_coin_from_register_dime(self):
        """"Test method for checking if Dime is returned from register"""
        money= self.soda_machine.get_coin_from_register('Dime')       
        self.assertEqual(money.name , "Dime")

    def test_get_coin_from_register_penny(self):
        """"Test method for checking if Penny is returned from register"""
        money= self.soda_machine.get_coin_from_register('Penny')       
        self.assertEqual(money.name , "Penny")

    def test_get_coin_from_register_invalid(self):
        """"Test method for checking if invald option is returned from register if bad option is inserted"""
        money= self.soda_machine.get_coin_from_register('Gold')       
        self.assertEqual(money, None)


class TestRegisterHasCoin(unittest.TestCase):
    """Testing method for register has coin"""
    def setUp(self):
        self.soda_machine= SodaMachine()

    def test_register_has_coin_quarter(self):
        """Test method for Quarter"""
        self.soda_machine.register_has_coin(Quarter())
        self.assertTrue(self.soda_machine.register_has_coin)

    def test_register_has_coin_dime(self):
        """Test method for Dime"""
        self.soda_machine.register_has_coin(Dime())
        self.assertTrue(self.soda_machine.register_has_coin)
    
    def test_register_has_coin_nickel(self):
        """Test method for nickel"""
        self.soda_machine.register_has_coin(Nickel())
        self.assertTrue(self.soda_machine.register_has_coin)

    def test_register_has_coin_penny(self):
        """Test method for penny"""
        self.soda_machine.register_has_coin(Penny())
        self.assertTrue(self.soda_machine.register_has_coin)

    def test_register_has_coin_string(self):
        """Test method for true or false"""
        self.soda_machine.register_has_coin("Nickle")
        self.assertTrue(self.soda_machine.register_has_coin)
    



if __name__ == '__main__':
    unittest.main()    