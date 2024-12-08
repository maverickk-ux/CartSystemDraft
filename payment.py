import customtkinter as ctk
import time
import threading
import random


class PaymentPage(ctk.CTkToplevel):
    def __init__(self, parent, receipt_details, go_to_home_callback):
        super().__init__(parent)
        self.title("Payment Page")
        self.geometry("500x500")

        self.receipt_details = receipt_details
        self.go_to_home_callback = go_to_home_callback
        self.payment_status = ctk.StringVar(value="Pending")
        self.transaction_id = None

        # Ensure window is on top
        self.lift()
        self.focus_force()

        # Receipt Display
        ctk.CTkLabel(self, text="Receipt Details:", font=("Arial", 14, "bold")).pack(pady=10)
        self.receipt_text = ctk.CTkTextbox(self, width=450, height=100)
        self.receipt_text.insert("1.0", self.receipt_details)
        self.receipt_text.configure(state="disabled")
        self.receipt_text.pack(pady=10)

        # Payment Method Selection
        ctk.CTkLabel(self, text="Select Payment Method:", font=("Arial", 12)).pack(pady=5)
        self.payment_method = ctk.StringVar(value="Credit Card")
        ctk.CTkOptionMenu(self, variable=self.payment_method,
                          values=["Credit Card", "Cash on Delivery", "UPI", "Wallet"]).pack(pady=10)

        # Progress Bar
        self.progress_label = ctk.CTkLabel(self, text="Payment Status: Pending", font=("Arial", 12))
        self.progress_label.pack(pady=5)
        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        # Buttons
        self.confirm_button = ctk.CTkButton(self, text="Confirm Payment", command=self.start_payment)
        self.confirm_button.pack(pady=10)

        self.cancel_button = ctk.CTkButton(self, text="Cancel Payment", command=self.cancel_payment, state="disabled")
        self.cancel_button.pack(pady=5)

        self.home_button = ctk.CTkButton(self, text="Go to Home", command=self.go_to_home_callback)
        self.home_button.pack(pady=5)

    def start_payment(self):
        self.transaction_id = f"TXN{random.randint(100000, 999999)}"  # Generate transaction ID
        self.confirm_button.configure(state="disabled")
        self.cancel_button.configure(state="normal")
        threading.Thread(target=self.process_payment).start()

    def process_payment(self):
        try:
            for i in range(1, 11):  # Simulate 10 steps of progress (approx 5-7 seconds)
                time.sleep(0.5)
                self.progress_bar.set(i / 10)
                self.progress_label.configure(text=f"Payment Status: {'Processing' if i < 10 else 'Completed'}")
                if self.payment_status.get() == "Failed":
                    break
            if self.payment_status.get() == "Failed":
                self.display_status("Failed", "red")
            else:
                self.payment_status.set("Completed")  # Explicitly set the payment status
                self.display_status("Completed", "green")
                self.show_thank_you_window()  # Open the Thank You window here
        finally:
            self.confirm_button.configure(state="normal")
            self.cancel_button.configure(state="disabled")

    def cancel_payment(self):
        self.payment_status.set("Failed")
        self.progress_label.configure(text="Payment Status: Failed")
        self.progress_bar.set(0)

    def display_status(self, status, color):
        ctk.CTkLabel(self, text=f"Payment {status}!", font=("Arial", 12, "bold"),
                     text_color=color).pack(pady=10)

    def show_thank_you_window(self):
        thank_you_window = ctk.CTkToplevel(self)
        thank_you_window.title("Thank You!")
        thank_you_window.geometry("400x300")

        # Ensure window is on top
        thank_you_window.lift()
        thank_you_window.focus_force()

        ctk.CTkLabel(thank_you_window, text="Thanks for Shopping!", font=("Arial", 24, "bold")).pack(pady=20)

        ctk.CTkButton(thank_you_window, text="Go to Home", command=self.go_to_home_callback).pack(pady=10)
        ctk.CTkButton(thank_you_window, text="FAQs", command=self.show_faq).pack(pady=10)

    def show_faq(self):
        faq_text = """FAQs:
1. What payment methods are supported?
   - Credit Card, UPI, Wallet, and Cash on Delivery.

2. Can I cancel a payment?
   - Yes, you can cancel during the payment process.

3. How do I check my transaction details?
   - Transaction ID is displayed after payment confirmation."""
        faq_window = ctk.CTkToplevel(self)
        faq_window.title("FAQs")
        faq_window.geometry("400x300")

        # Ensure FAQ window appears on top
        faq_window.lift()
        faq_window.focus_force()

        ctk.CTkLabel(faq_window, text="Frequently Asked Questions", font=("Arial", 14, "bold")).pack(pady=10)
        faq_textbox = ctk.CTkTextbox(faq_window, width=350, height=200)
        faq_textbox.insert("1.0", faq_text)
        faq_textbox.configure(state="disabled")
        faq_textbox.pack(pady=10)


# Test Script
if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Use system light/dark mode
    ctk.set_default_color_theme("blue")  # Default color theme

    def go_to_home():
        print("Returning to Home Page...")

    # Simulated Receipt
    receipt_details = """
Item 1: ₹500
Item 2: ₹300
Discount: ₹50
-------------------
Total: ₹750
"""

    root = ctk.CTk()
    root.title("Main Application")
    root.geometry("500x500")

    def open_payment_page():
        PaymentPage(root, receipt_details, go_to_home)

    # Button to Open Payment Page
    open_button = ctk.CTkButton(root, text="Open Payment Page", command=open_payment_page)
    open_button.pack(pady=20)

    root.mainloop()
