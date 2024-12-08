import json
import os
import customtkinter as ctk


class Cart:
    def __init__(self, username, cart_file="cart.json"):
        self.username = username
        self.cart_file = cart_file
        self.cart = self.load_cart()

    def load_cart(self):
        """Load the cart from the JSON file."""
        if os.path.exists(self.cart_file):
            if os.path.getsize(self.cart_file) == 0:  # Check if file is empty
                return {}
            with open(self.cart_file, "r") as file:
                try:
                    users = json.load(file)
                    return users.get(self.username, {})
                except json.JSONDecodeError:
                    print("Error: Cart file is corrupted. Initializing a new cart.")
                    return {}
        return {}


    def save_cart(self):
        if os.path.exists(self.cart_file):
            with open(self.cart_file, "r") as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    users = {}
        else:
            users = {}

        users[self.username] = self.cart

        with open(self.cart_file, "w") as file:
            json.dump(users, file, indent=4)

    def view_cart(self):
        cart_window = ctk.CTkToplevel()
        cart_window.title(f"{self.username}'s Cart")
        cart_window.geometry("400x400")

        row = 0
        for product, details in self.cart.items():
            ctk.CTkLabel(
                cart_window, text=f"{product} - Qty: {details['quantity']} - Price: ${details['price']:.2f}"
            ).grid(row=row, column=0, padx=10, pady=5)
            row += 1
    
    def calculate_total_price(self):
        """Calculate the total price of the cart based on the nested dictionary."""
        total_price = 0
        for product, details in self.cart.items():
            # Calculate price per product (quantity * price) and sum it up
            total_price += details["quantity"] * details["price"]
        return total_price

    def add_item(self, item_name, item_price):
        if item_name in self.cart:
            self.cart[item_name]["quantity"] += 1
        else:
            self.cart[item_name] = {"quantity": 1, "price": item_price}
        self.save_cart()

    def remove_item(self, item_name):
        if item_name in self.cart:
            self.cart[item_name]["quantity"] -= 1
            if self.cart[item_name]["quantity"] <= 0:
                del self.cart[item_name]
            self.save_cart()

    def get_cart(self):
        """Return the current cart."""
        return self.cart
