# import json
# class admin:
#     def __init__(self):
#         self.food = {}
#         self.food_id = len(self.food) +1

#     def add_food_item(self):
#         self.name = input("Enter the name of the food item ")
#         self.quantity = int(input("enter the quantity of the food item"))
#         self.price = int(input("Enter the price of the food item"))
#         self.stock = int(input("Enter the stock of the food item"))
#         self.discount = int(input("Enter the discount of food item"))
#         self.item = {"name": self.name, "quantity": self.quantity,"price": self.price,"stock": self.stock,"discount":self.discount}
#         self.food_id = len(self.food) + 1
#         self.food[self.food_id] = self.item
#         with open("food_item.json","w") as f:
#             json.dump(self.food, f)

#         x=admin()
#         x.add_food_item()
#         x.add_food_item()

import random

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class RestaurantMenu:
    def __init__(self):
        self.food_items = []

    def add_food_item(self):
        name = input("Enter the name of the food item: ")
        quantity = input("Enter the quantity of the food item: ")
        price = float(input("Enter the price of the food item: "))
        discount = float(input("Enter the discount for the food item (in decimal): "))
        stock = int(input("Enter the stock of the food item: "))
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully.")

    def edit_food_item(self):
        food_id = int(input("Enter the FoodID of the food item you want to edit: "))
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                name = input("Enter the new name of the food item: ")
                quantity = input("Enter the new quantity of the food item: ")
                price = float(input("Enter the new price of the food item: "))
                discount = float(input("Enter the new discount for the food item (in decimal): "))
                stock = int(input("Enter the new stock of the food item: "))
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item edited successfully.")
                break
        else:
            print("Food item not found in the menu.")

    def view_food_items(self):
        if not self.food_items:
            print("No food items in the menu.")
        else:
            for food_item in self.food_items:
                print("Food ID:", food_item.food_id)
                print("Name:", food_item.name)
                print("Quantity:", food_item.quantity)
                print("Price:", food_item.price)
                print("Discount:", food_item.discount)
                print("Stock:", food_item.stock)
                print("-------------------------")

    def remove_food_item(self):
        food_id = int(input("Enter the FoodID of the food item you want to remove: "))
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully.")
                break
        else:
            print("Food item not found in the menu.")

# Test the functionality
menu = RestaurantMenu()

while True:
    print("Menu Options:")
    print("1. Add new food item")
    print("2. Edit food item")
    print("3. View all food items")
    print("4. Remove food item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        menu.add_food_item()
    elif choice == '2':
        menu.edit_food_item()
    elif choice == '3':
        menu.view_food_items()
    elif choice == '4':
        menu.remove_food_item()
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
