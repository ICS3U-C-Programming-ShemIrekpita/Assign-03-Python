#!/usr/bin/env python3
# Created by: Shem
# Created on: 11/5/2025
# This code takes the order of pizza
# with toppings and calculates the price
def main():
# Constants
    ChickenTopping = 3.00
    BeefTopping = 2.00
    VegetableTopping = 1.10
    SmallPizza = 10.00
    LargePizza = 16.00
    ExtraLargePizza = 25.00
    HST = 0.13
# Display pizza selection
    print("Welcome to Shem's Pizza Shop!")
    print("Pick a selection:")
    print("1: Small pizza + Chicken Topping")
    print("2: Small pizza + Beef Topping")
    print("3: Small pizza + Vegetable Topping")
    print("4: Large pizza + Chicken Topping")
    print("5: Large pizza + Beef Topping")
    print("6: Large pizza + Vegetable Topping")
    print("7: Extra-large pizza + Chicken Topping")
    print("8: Extra-large pizza + Beef Topping")
    print("9: Extra-large pizza + Vegetable Topping")
# Ask for pizza selection
    selection = input("Enter a selection (1-9): ")
    selection_description = ""
    if selection == "1":
        base_price = SmallPizza + ChickenTopping
        selection_description = "Small pizza + Chicken Topping"
    elif selection == "2":
        base_price = SmallPizza + BeefTopping
        selection_description = "Small pizza + Beef Topping"
    elif selection == "3":
        base_price = SmallPizza + VegetableTopping
        selection_description = "Small pizza + Vegetable Topping"
    elif selection == "4":
        base_price = LargePizza + ChickenTopping
        selection_description = "Large pizza + Chicken Topping"
    elif selection == "5":
        base_price = LargePizza + BeefTopping
        selection_description = "Large pizza + Beef Topping"
    elif selection == "6":
        base_price = LargePizza + VegetableTopping
        selection_description = "Large pizza + Vegetable Topping"
    elif selection == "7":
        base_price = ExtraLargePizza + ChickenTopping
        selection_description = "Extra-large pizza + Chicken Topping"
    elif selection == "8":
        base_price = ExtraLargePizza + BeefTopping
        selection_description = "Extra-large pizza + Beef Topping"
    elif selection == "9":
        base_price = ExtraLargePizza + VegetableTopping
        selection_description = "Extra-large pizza + Vegetable Topping"
    else:
        print("Enter a selection Number.")
# Calculate subtotal, tax, and total
    subtotal = base_price
    tax = subtotal * HST
    total = subtotal + tax
    print("You selected:", selection_description)
    print("Subtotal: ${:,.2f}".format(subtotal))
    print("Tax: ${:,.2f}".format(tax))
    print("Your total is ${:,.2f}".format(total))
    print("Thank you for ordering from Shem's Pizza Shop!")

if __name__ == "__main__":
    main()
