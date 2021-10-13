import unittest
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    
    def setUp(self):
        self.soda_machine= SodaMachine()



    def test_filling_register(self):
        register_total= self.soda_machine.register

        self.assertEqual(len(register_total), 88)







if __name__ == '__main__':
    unittest.main()    