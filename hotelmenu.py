#Define the menu of restaurant

menu = {
    "Pizza":40,
    "Pasta":50,
    "Burger":60,
    "Salad":70,
    "Coffee":80
}
#Greet
print("Welcome to our PYTHON restaurant")
print("Pizza: Rs.40\nPasta: Rs.50\nBurger: Rs.60\nSalad: Rs.70\nCoffee: Rs.80")

total_order = 0

item1 = input("Enter the name of the Item you want to order:")
if item1 in menu:
    total_order+= menu[item1] #0 + item Prize
    print(f"Your Item {item1} has been added to your order:")
else:
    print(f"Order Item {item1} is not Available")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item2 = input("Enter the name of the second Item you want to order:")
    if item2 in menu:
        total_order+= menu[item2] #0 + item Prize
        print(f"Your Item {item2} has been added to your order:")
    else:
        print(f"Order Item {item2} is not Available")
    
print(f"The Total Amount of Item is {total_order}")