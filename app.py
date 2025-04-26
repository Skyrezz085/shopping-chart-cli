"""
=================================================
Simple Shopping Cart Program (CLI-based)

This program demonstrates basic Python concepts like:
- Conditionals
- Loops
- Functions
- Object-Oriented Programming (OOP)

It simulates a shopping cart system in the command line.
=================================================
"""

class CartItem:
    """
    Represents a single item in the shopping cart.

    Attributes:
    ----------
    name : str
        The item's name.
    price : float
        The item's price.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    """
    A simple shopping cart system.

    Attributes:
    ----------
    items : list
        A list to store CartItem objects.

    Methods:
    -------
    add_item(item): Add an item to the cart.
    remove_item(name): Remove an item by name.
    total_price(): Calculate total cost of items.
    show_cart(): Show all items in the cart.
    run(): Start the shopping cart menu.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the cart."""
        self.items.append(item)
        print(f'Item "{item.name}" has been added to your cart.')

    def remove_item(self, name):
        """Remove an item from the cart by name."""
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f'Item "{name}" has been removed from your cart.')
                return
        print(f'Item "{name}" not found in your cart.')

    def total_price(self):
        """Return the total price of all items."""
        return sum(item.price for item in self.items)

    def show_cart(self):
        """Display the items in the cart."""
        if not self.items:
            print("Your shopping cart is empty.")
            return

        print("\nItems in your cart:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item.name} - Rp {item.price:,.2f}")

    def run(self):
        """Run the command-line shopping cart menu."""
        print("Welcome to Toko Leuwi Leutik!")

        while True:
            print("\nMenu:")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. View Cart")
            print("4. View Total Price")
            print("5. Exit")

            choice = input("Select an option (1-5): ")

            if choice == '1':
                name = input("Enter item name: ")
                try:
                    price = float(input("Enter item price: "))
                    item = CartItem(name, price)
                    self.add_item(item)
                except ValueError:
                    print("Invalid price. Please enter a number.")

            elif choice == '2':
                name = input("Enter the name of the item to remove: ")
                self.remove_item(name)

            elif choice == '3':
                self.show_cart()

            elif choice == '4':
                total = self.total_price()
                print(f"Total price: Rp {total:,.2f}")

            elif choice == '5':
                print("Thank you for shopping at Toko Leuwi Leutik!")
                break

            else:
                print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.run()