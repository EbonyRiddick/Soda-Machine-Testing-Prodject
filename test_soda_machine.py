import unittest
from soda_machine import SodaMachine

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








if __name__ == '__main__':
    unittest.main()    