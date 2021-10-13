import unittest
from soda_machine import SodaMachine
from coins import Quarter, Nickel, Dime, Penny


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

    
    def test_fill_inventory(self):
        inventory_total= self.soda_machine.inventory

        self.assertEqual(len(inventory_total), 30)


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