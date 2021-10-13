import unittest


import unittest
from wallet import Wallet

class TestWallet(unittest.TestCase):
    """"Tests for wallet method that creates money list"""

    def setUp(self): 
        self.user_wallet= Wallet()

    def testwalletlenght(self):
        wallet_total= self.user_wallet.money
        self.assertEqual(len(wallet_total), 88)

if __name__ == '__main__':
    unittest.main()