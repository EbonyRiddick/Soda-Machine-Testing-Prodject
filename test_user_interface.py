import unittest
import user_interface
from coins import Quarter, Dime, Nickel, Penny
from cans import Cola, OrangeSoda, RootBeer

class TestUserInterface(unittest.TestCase):
    """Testing functions within the user interface"""

    def test_validate_main_menu_one(self):
        self.user_interface = user_interface
        user_input = self.user_interface.validate_main_menu(1)
        self.assertEqual(user_input, (True, 1))


    def test_validate_main_mene_two(self):
        self.user_interface = user_interface
        user_input = self.user_interface.validate_main_menu(2)
        self.assertEqual(user_input, (True, 2))

    def test_validate_main_menu_three(self):
        self.user_interface = user_interface
        user_input = self.user_interface.validate_main_menu(3)
        self.assertEqual(user_input, (True, 3))

    def test_validate_main_menu_four(self):
        self.user_interface = user_interface
        user_input = self.user_interface.validate_main_menu(4)
        self.assertEqual(user_input, (True, 4))

    def test_validate_main_menu_five(self):
        self.user_interface = user_interface
        user_input = self.user_interface.validate_main_menu(5)
        self.assertEqual(user_input, (False, None))


class TestTryParseInt(unittest.TestCase):
    """Test method for try Parse Int"""

    def test_try_parse_int_number_as_string(self):
        self.user_interface = user_interface
        user_input= self.user_interface.try_parse_int('10')
        self.assertEqual(user_input, 10)


    def test_try_parse_int_random_string(self):
        self.user_interface = user_interface
        user_input= self.user_interface.try_parse_int('hello')
        self.assertEqual(user_input, 0)
















class TestDisplayPaymentValue(unittest.TestCase):
    """Test method for displaying payment value"""

    def test_display_payment_value_all_coin_types(self):
        self.user_interface = user_interface
        coin_list=[Quarter(), Nickel(), Dime(), Penny()]
        coin_total_value= self.user_interface.display_payment_value(coin_list)
        self.assertEqual(coin_total_value, .41)


    def test_display_payment_value_no_coins(self):

    
        self.user_interface = user_interface
        coin_list=[]
        coin_total_value= self.user_interface.display_payment_value(coin_list)
        self.assertEqual(coin_total_value, .00)




class TestValidateCoinSelection(unittest.TestCase):
    """"Test methods for validationg coin selection 1-5"""

    def test_validate_coin_selection_one(self):
        self.user_interface = user_interface
        user_input= self.user_interface.validate_coin_selection(1)
        self.assertEqual(user_input, (True, 'Quarter'))

    def test_validate_coin_selection_two(self):
        self.user_interface = user_interface
        user_input= self.user_interface.validate_coin_selection(2)
        self.assertEqual(user_input, (True, 'Dime'))

    def test_validate_coin_selection_three(self):
        self.user_interface = user_interface
        user_input= self.user_interface.validate_coin_selection(3)
        self.assertEqual(user_input, (True, 'Nickel'))


    def test_validate_coin_selection_four(self):
        self.user_interface = user_interface
        user_input= self.user_interface.validate_coin_selection(4)
        self.assertEqual(user_input, (True, 'Penny'))

    def test_validate_coin_selection_five(self):
        self.user_interface = user_interface
        user_input= self.user_interface.validate_coin_selection(5)
        self.assertEqual(user_input, (True, 'Done'))    
    
    def test_validate_coin_selection_six(self):
        """"Tests wrong number input"""
        self.user_interface = user_interface
        user_input= self.user_interface.validate_coin_selection(6)
        self.assertEqual(user_input, (False, None))  
    

if __name__ == '__main__':
    unittest.main()