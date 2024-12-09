# CartSystemDraft
This is the a draft of Cart System Project.
Login Page -> Main Page -> Electronics/Clothing/Groceries -> View Cart -> Checkout
(First three steps done)

E-Commerce Cart System - Team 8

Team members: 
	1. K V Shashank Pai - BT2024250
	2. Yash Sultania - BT2024013
	3. Ravi Abhinav - BT2024239
	4. Hasini Yamsani - BT2024133

Project Summary:
This project is a simple yet powerful eCommerce cart system built to manage products, quantities, and user orders. It allows users to add products to their cart, view the contents, update quantities, and remove items. The system integrates seamlessly with a checkout process, providing an efficient and user-friendly shopping experience. 

Features: 
Add to Cart: Users can add multiple items to their shopping cart.
Update Quantity: The quantity of items in the cart can be updated.
Remove Items: Items can be removed from the cart at any time.
View Cart: Users can view their cart’s contents with details like product name, price, and quantity.
Data backup: Users don't lose their cart even after exiting our interface as all data are stored efficiently in our json database in the form of nested dictionary which contains the following format~ {<username>:{<product1>:{<quantity>:q1,<price1>:p1},<product2>:{quantity>q2,<price2:p2>}}}

Steps to Use:
1. The program begins with the Login Page. Provide your username and password. If your account exists and the password is correct, you are directed to the main page. Else a signup option is available for conveniently making a new account with us.
2. In the main page you are provided with three categories of products which our cart system facilitates. Select the one you are looking for. (Electronics/Clothing/Groceries)
	I) Electronics page - Contains a list of electronic products which can be added to cart using the (add) '+' button and removed 			using the (remove) '-' button. Additionally the warranty period of each product is displayed at the bottom of each product 		for our users to keep a track of their warranty.
	II) Clothing Page - Contains a list of clothing products which can be added to cart using the (add) '+' button and removed using 		the (remove) '-' button. Furthermore, two drop down menus for color and size respectively are provided for users to select 		the appropriate product.
	III) Grocery page - Contains a list of grocery products which can be added to cart using the (add) '+' button and removed using 		the (remove) '-' button. Additionally the expiry date for each product is given below it.

	NOTE: At each point of changes in cart, the total price is displayed at the bottom right of the screen to help users keep a track of billing cost.
3. Moving to the checkout page gives a overall review about your cart with all items displayed together. Users have yet another chance to modify the quantity of products using the + and - buttons provided. If they wish to proceed they can click the proceed to payment button.
4. The final page is the payment page. Here the total price is shown along with a drop down menu of mode of payment (UPI/card/new banking). Click the complete payment to finish transaction and buy your products.

Libraries used: 
1. json - For reading and writing user data to a JSON file (e.g., users.json).
2. tkinter and customtkinter - For creating GUI components like windows, labels, and buttons.
3. warnings - Used implicitly in customtkinter for warning messages.
4. os (if you're managing file paths or external files, though not explicitly shown in the code).

work division: 
Login Page, main page - Shashank
Checkout page, cart page - Yash Sultania
groceries page, clothing page, electronics page - Hasini
payment page - Abhinav

