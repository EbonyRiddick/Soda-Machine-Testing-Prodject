import unittest
from soda_machine import SodaMachine
from coins import Quarter, Dime, Nickel, Penny
from cans import Cola, OrangeSoda, RootBeer

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
        money= Quarter()
        self.soda_machine.get_coin_from_register(money)       
        self.assertEqual(money.name , "Quarter")
      
    def test_get_coin_from_register_nickel(self):
        """"Test method for checking if Nickel is returned from register"""
        money= Nickel()
        self.soda_machine.get_coin_from_register(money)       
        self.assertEqual(money.name , "Nickel")

    def test_get_coin_from_register_dime(self):
        """"Test method for checking if Dime is returned from register"""
        money= Dime()
        self.soda_machine.get_coin_from_register(money)       
        self.assertEqual(money.name , "Dime")

    def test_get_coin_from_register_penny(self):
        """"Test method for checking if Penny is returned from register"""
        money= Penny()
        self.soda_machine.get_coin_from_register(money)       
        self.assertEqual(money.name , "Penny")

    def test_get_coin_from_register_invalid(self):
        """"Test method for checking if invald option is returned from register if bad option is inserted"""
        money= self.soda_machine.get_coin_from_register('Gold')       
        self.assertIsNone(money)


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
    

class DetermineChangeValue(unittest.TestCase):
    """Testing method used to determine change value"""

    def setUp(self):
        self.soda_machine= SodaMachine()

    def test_determine_change_value_total_payment_higher(self):
        """Testing with total payment higher"""
        change = self.soda_machine.determine_change_value(2,.65)
        self.assertEqual(change,1.35)

    def test_determine_change_value_soda_price_higher(self):
        """Testing with soda price higher"""
        change = self.soda_machine.determine_change_value(.60,.75)
        self.assertEqual(change, -.15)

    def test_determine_change_value_equal(self):
        """Testing with equal values"""
        change = self.soda_machine.determine_change_value(.60,.60)
        self.assertEqual(change,0)

class TestCalculateCoinValue(unittest.TestCase):
    def setUp(self):
        self.soda_machine= SodaMachine()

    def test_calculate_coin_value(self):
        """"Test Calculate coin value method for proper calculations"""
        coin_list=[Quarter(), Nickel(), Dime(), Penny()]

        total= self.soda_machine.calculate_coin_value(coin_list)

        self.assertEqual(total, 0.41)

    def test_calculate_coin_value(self):
        """""Test calculate coin value method to get zero if empty string is inserted"""
        coin_list=[]

        total= self.soda_machine.calculate_coin_value(coin_list)

        self.assertEqual(total, 0)


class TestGetInventorySoda(unittest.TestCase):
    """"Test method for insuring that soda can that is called gets returned"""
    def setUp(self):
        self.soda_machine= SodaMachine()

    def test_get_inventory_soda_cola(self):
        """"Test method that returneds cola"""
        soda= Cola()
        self.soda_machine.get_inventory_soda(soda)
        self.assertEqual(soda.name, 'Cola')

    def test_get_inventory_soda_orange_soda(self):
        """"Test method that returneds Orange Soda"""
        soda= OrangeSoda()
        self.soda_machine.get_inventory_soda(soda)
        self.assertEqual(soda.name, 'Orange Soda')

    def test_get_inventory_soda_root_beer(self):
        """"Test method that returneds Root Beer"""
        soda= RootBeer()
        self.soda_machine.get_inventory_soda(soda)
        self.assertEqual(soda.name, 'Root Beer')    

    def test_get_inventory_soda_root_beer(self):
        """"Test method that returneds a none value"""
        soda= self.soda_machine.get_inventory_soda('Mountian Dew')
        self.assertIsNone(soda)  

        
class TestReturnInventory(unittest.TestCase):
    """Testing return inventory method to make sure after attempted purchase fails can is added back to inventory"""

<<<<<<< HEAD
class TestReturnInventory(unittest.TestCase):
    """Testing return inventory method to make sure after attempted purchase fails can is added back to inventory"""
=======
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_return_inventory(self):
        can = RootBeer()
        self.soda_machine.return_inventory(can)
        self.assertEqual(len(self.soda_machine.inventory), 31)




















>>>>>>> 96bc139ce510bd370c839f1ac340a0688a50cd68





class TestDepositCoinsIntoRegister(unittest.TestCase):
    """Test method for Deposit coins into Register"""
    def setUp(self):
        self.soda_machine= SodaMachine()


    def test_deposit_coins_into_register(self):

        coin_list= [Quarter(), Dime(), Nickel(), Penny()] 
        
        self.soda_machine.deposit_coins_into_register(coin_list)
        self.assertEqual(len(self.soda_machine.register), 92)




if __name__ == '__main__':
    unittest.main()    