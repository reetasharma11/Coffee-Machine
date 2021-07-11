MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']


def ask_money():
    print("please insert coins.")
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickle = int(input("how many nickles?: "))
    penny = int(input("how many pennies"))
    total_amount = quarter * 0.25 + dime * 0.10 + nickle * 0.05 + penny * 0.01
    return total_amount


is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino):")

    if order == "report":
        print(f"water: {water}")
        print(f"milk: {milk}")
        print(f"coffee: {coffee}")
        print(f"money: {profit}")

    elif order == "espresso":
        if water >= MENU["espresso"]["ingredients"]["water"] and \
                coffee >= MENU["espresso"]["ingredients"]["coffee"]:
            total_amount = ask_money()
            return_amount = total_amount - MENU["espresso"]["cost"]
            change = round(return_amount, 3)
            print(f"Here is {change}$ in change.")
            if total_amount >= MENU["espresso"]["cost"]:
                profit += MENU["espresso"]["cost"]
                water -= MENU["espresso"]["ingredients"]["water"]
                coffee -= MENU["espresso"]["ingredients"]["coffee"]
                print("Here is your espresso.Enjoy it!")
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("Sorry there is not enough water.")
    elif order == "latte":
        if water >= MENU["latte"]["ingredients"]["water"] and \
                milk >= MENU["latte"]["ingredients"]["milk"] and \
                coffee >= MENU["latte"]["ingredients"]["coffee"]:
            total_amount = ask_money()
            return_amount = total_amount - MENU["latte"]["cost"]
            change = round(return_amount, 3)
            print(f"Here is {change}$ in change.")
            if total_amount >= MENU["latte"]["cost"]:
                profit += MENU["latte"]["cost"]
                water -= MENU["latte"]["ingredients"]["water"]
                milk -= MENU["latte"]["ingredients"]["milk"]
                coffee -= MENU["latte"]["ingredients"]["coffee"]
                print("Here is your latte.Enjoy it!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough water.")

    elif order == "cappuccino":
        if water >= MENU["cappuccino"]["ingredients"]["water"]:
            total_amount = ask_money()
            return_amount = total_amount - MENU["cappuccino"]["cost"]
            change = round(return_amount, 3)
            print(f"Here is {change}$ in change.")
            if total_amount >= MENU["cappuccino"]["cost"]:
                profit += MENU["cappuccino"]["cost"]
                water -= MENU["cappuccino"]["ingredients"]["water"]
                milk -= MENU["cappuccino"]["ingredients"]["milk"]
                coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
                print("Here is your cappuccino.Enjoy it!")
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("Sorry there is not enough water.")

    elif order == "off":
        is_on = False
