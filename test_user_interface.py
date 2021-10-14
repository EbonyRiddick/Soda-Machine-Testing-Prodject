import unittest
import user_interface

class TestUserInterface(unittest.TestCase):
    """Testing functions within the user interface"""

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


if __name__ == '__main__':
    unittest.main()