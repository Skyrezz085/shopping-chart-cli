"""
=================================================
This script simulates a simple shopping cart system 
through a command-line interface (CLI) and 
contains unit tests for the ShoppingCart class.
=================================================
"""

import unittest
from reza_app import CartItem, ShoppingCart

class TestShoppingCart(unittest.TestCase):
    """
    This class contains unit tests for the ShoppingCart class
    to verify that core features work correctly.
    """

    def setUp(self):
        """
        This method runs before each test case.
        It creates a ShoppingCart and sample CartItem objects.
        """
        self.cart = ShoppingCart()
        self.item1 = CartItem("Apple", 3400)
        self.item2 = CartItem("Orange", 2100)

    def test_add_item(self):
        """
        Test if items are added correctly to the cart.
        """
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)

        # Verify that the cart contains 2 items
        self.assertEqual(len(self.cart.items), 2)

        # Verify the names of the added items
        self.assertEqual(self.cart.items[0].name, "Apple")
        self.assertEqual(self.cart.items[1].name, "Orange")

    def test_remove_item(self):
        """
        Test if an item is removed correctly from the cart.
        """
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.cart.remove_item("Apple")

        # After removal, only one item should remain
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, "Orange")

    def test_total_price(self):
        """
        Test if the total price of items is calculated correctly.
        """
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        total = self.cart.total_price()

        # Expected total: 3400 + 2100 = 5500
        self.assertEqual(total, 5500)


# Run the tests if this file is executed directly
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)