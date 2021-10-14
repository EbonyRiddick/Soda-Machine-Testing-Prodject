import unittest
import user_interface
from coins import Quarter, Dime, Nickel, Penny
from cans import Cola, OrangeSoda, RootBeer

class TestUserInterface(unittest.TestCase):
    """Testing functions within the user interface 1-5"""

    def test_validate_main_menu(self):
        self.user_interface = user_interface
        user_input = self.user_interface.validate_main_menu(1)
        self.assertEqual(user_input, (True, 1))


    def test_validate_main_menu(self):
        self.user_interface = user_interface
        user_input = self.user_interface.validate_main_menu(2)
        self.assertEqual(user_input, (True, 2))

    def test_validate_main_menu(self):
        self.user_interface = user_interface
        user_input = self.user_interface.validate_main_menu(3)
        self.assertEqual(user_input, (True, 3))

    def test_validate_main_menu(self):
        self.user_interface = user_interface
        user_input = self.user_interface.validate_main_menu(4)
        self.assertEqual(user_input, (True, 4))

    def test_validate_main_menu(self):
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


class TestGetUniqueCanName(unittest.TestCase):
    """Testing return of can names"""

    def test_get_unique_can_name(self):
        cans_list = [Cola(), Cola(), RootBeer(), RootBeer(), OrangeSoda(), OrangeSoda()]
        self.user_interface = user_interface
        unique_name = self.user_interface.get_unique_can_names(cans_list)
        self.assertEqual(len(unique_name), 3)

    def test_get_unique_can_name_empty_list(self):
        cans_list = []
        self.user_interface = user_interface
        unique_name = self.user_interface.get_unique_can_names(cans_list)
        self.assertEqual(len(unique_name), 0)


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




if __name__ == '__main__':
    unittest.main()