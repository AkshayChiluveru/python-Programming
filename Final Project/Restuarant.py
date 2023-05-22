import json

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class RestaurantMenu:
    def __init__(self):
        self.food_items = []

    def add_food_item(self):
        name = input("Enter the food item name: ")
        quantity = input("Enter the quantity of the food item: ")
        price = float(input("Enter the price of the food item: "))
        discount = float(input("Enter the discount on the food item (%): "))
        stock = int(input("Enter the stock amount of the food item: "))

        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = len(self.food_items) + 1
        self.food_items.append(food_item)
        print("Food item added successfully.")

    def edit_food_item(self):
        food_id = int(input("Enter the food item ID to edit: "))
        food_item = self.get_food_item(food_id)
        if food_item is None:
            print("Food item not found.")
        else:
            print("Current Details:")
            self.display_food_item(food_item)
            print("Enter new details:")
            name = input("Enter the new name of the food item: ")
            quantity = input("Enter the new quantity of the food item: ")
            price = float(input("Enter the new price of the food item: "))
            discount = float(input("Enter the new discount on the food item (%): "))
            stock = int(input("Enter the new stock amount of the food item: "))

            food_item.name = name
            food_item.quantity = quantity
            food_item.price = price
            food_item.discount = discount
            food_item.stock = stock
            print("Food item updated successfully.")

    def view_food_items(self):
        if not self.food_items:
            print("No food items in the menu.")
        else:
            print("Food Items:")
            for food_item in self.food_items:
                self.display_food_item(food_item)

    def remove_food_item(self):
        food_id = int(input("Enter the food item ID to remove: "))
        food_item = self.get_food_item(food_id)
        if food_item is None:
            print("Food item not found.")
        else:
            self.food_items.remove(food_item)
            print("Food item removed successfully.")

    def display_food_item(self, food_item):
        print(f"Food ID: {food_item.food_id}")
        print(f"Name: {food_item.name}")
        print(f"Quantity: {food_item.quantity}")
        print(f"Price: {food_item.price}")
        print(f"Discount: {food_item.discount}%")
        print(f"Stock: {food_item.stock}")

    def get_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                return food_item
        return None

    def save_menu_to_json(self, fooditem):
        data = {
            "food_items": [
                {
                    "FoodID": food_item.food_id,
                    "Name": food_item.name,
                    "Quantity": food_item.quantity,
                    "Price": food_item.price,
                    "Discount": food_item.discount,
                    "Stock": food_item.stock
                }
                for food_item in self.food_items
            ]
        }
        with open("fooditem.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Menu saved to {fooditem}.")

    def load_menu_from_json(self, fooditem):
        try:
            with open("fooditem.json", "r") as file:
                data = json.load(file)

            self.food_items = [
                FoodItem(
                    item["Name"],
                    item["Quantity"],
                    item["Price"],
                    item["Discount"],
                    item["Stock"]
                )
                for item in data["food_items"]
            ]
            print(f"Menu loaded from {fooditem}.")
        except FileNotFoundError:
            print(f"File '{fooditem}' not found. Starting with an empty menu.")

class User:
    def __init__(self, full_name, phone_number, email, password ,address):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.address = address

class RestaurantApp:
    def __init__(self):
        self.menu = RestaurantMenu()
        self.users = []
        self.orders = []

    def register(self):
        full_name = input("Enter your full name: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        address = input("Enter your address: ")

        user = User(full_name, phone_number, email, password , address)
        self.users.append(user)
        print("Registration successful.")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in self.users:
            if user.email == email and user.password == password:
                print("Login successful.")
                return user

        print("Invalid email or password.")
        return None

    def place_new_order(self, user):
        print("Food Items:")
        self.menu.view_food_items()

        selected_items = input("Enter the numbers of the food items to order (separated by commas): ")
        selected_items = [int(item) for item in selected_items.split(",")]

        order_items = []
        for item in selected_items:
            food_item = self.menu.get_food_item(item)
            if food_item is not None:
                order_items.append(food_item)

        if not order_items:
            print("No items selected. Order placement canceled.")
            return

        print("Selected Items:")
        for food_item in order_items:
            self.menu.display_food_item(food_item)

        confirm_order = input("Do you want to place the order? (yes/no): ")
        if confirm_order.lower() == "yes":
            order = (user, order_items)
            self.orders.append(order)
            print("Order placed successfully.")
        else:
            print("Order placement canceled.")

    def order_history(self, user):
        user_orders = [order for order in self.orders if order[0] == user]

        if not user_orders:
            print("No order history.")
        else:
            print("Order History:")
            for order in user_orders:
                print("Order Items:")
                for food_item in order[1]:
                    self.menu.display_food_item(food_item)
                print()

    def update_profile(self, user):
        print("Current Profile:")
        print(f"Full Name: {user.full_name}")
        print(f"Phone Number: {user.phone_number}")
        print(f"Email: {user.email}")
        print(f"Address: {user.address}")
        print("Enter new details:")

        full_name = input("Enter the new full name: ")
        phone_number = input("Enter the new phone number: ")
        address = input("Enter the new address: ")

        user.full_name = full_name
        user.phone_number = phone_number
        user.address = address

        print("Profile updated successfully.")

    def run(self):
        menu_filename = "menu.json"

        self.menu.load_menu_from_json(menu_filename)

        while True:
            print("1. Admin")
            print("2. User")
            print("3. Exit")

            choice = input("Select an option: ")
            if choice == "1":
                admin_password = input("Enter the admin password: ")
                if admin_password == "admin":
                    while True:
                        print("1. Add Food Item")
                        print("2. Edit Food Item")
                        print("3. View Food Items")
                        print("4. Remove Food Item")
                        print("5. Save Menu to JSON")
                        print("6. Exit")

                        admin_choice = input("Select an option: ")
                        if admin_choice == "1":
                            self.menu.add_food_item()
                        elif admin_choice == "2":
                            self.menu.edit_food_item()
                        elif admin_choice == "3":
                            self.menu.view_food_items()
                        elif admin_choice == "4":
                            self.menu.remove_food_item()
                        elif admin_choice == "5":
                            self.menu.save_menu_to_json(menu_filename)
                        elif admin_choice == "6":
                            break
                        else:
                            print("Invalid choice. Try again.")
                else:
                    print("Incorrect admin password.")
            elif choice == "2":
                while True:
                    print("1. Register")
                    print("2. Log in")
                    print("3. Place New Order")
                    print("4. Order History")
                    print("5. Update Profile")
                    print("6. Exit")

                    user_choice = input("Select an option: ")
                    if user_choice == "1":
                        self.register()
                    elif user_choice == "2":
                        user = self.login()
                        if user is not None:
                            while True:
                                print("1. Place New Order")
                                print("2. Order History")
                                print("3. Update Profile")
                                print("4. Logout")

                                user_option = input("Select an option: ")
                                if user_option == "1":
                                    self.place_new_order(user)
                                elif user_option == "2":
                                    self.order_history(user)
                                elif user_option == "3":
                                    self.update_profile(user)
                                elif user_option == "4":
                                    break
                                else:
                                    print("Invalid choice. Try again.")
                        else:
                            print("Login failed. Please try again.")
                    elif user_choice == "3":
                        print("Please register or log in first.")
                    elif user_choice == "4":
                        print("Please register or log in first.")
                    elif user_choice == "5":
                        print("Please register or log in first.")
                    elif user_choice == "6":
                        break
                    else:
                        print("Invalid choice. Try again.")
            elif choice == "3":
                self.menu.save_menu_to_json(menu_filename)
                break
            else:
                print("Invalid choice. Try again.")

app = RestaurantApp()
app.run()
