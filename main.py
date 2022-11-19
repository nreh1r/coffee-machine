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


def check_water(order):
    return MENU[order]["ingredients"]["water"] <= resources["water"]


def check_milk(order):
    return MENU[order]["ingredients"]["milk"] <= resources["milk"]


def check_coffee(order):
    return MENU[order]["ingredients"]["coffee"] <= resources["coffee"]


running = True

while running:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "exit":
        running = False
        continue
    elif order == "report":
        for resource in resources:
            if resource == "water" or resource == "milk":
                print(f"{resource.title()}: {resources[resource]}ml")
            elif resource == "coffee":
                print(f"{resource.title()}: {resources[resource]}g")
            elif resource == "money":
                print(f"{resource.title()}: ${resources[resource]:.2f}")
        if "money" not in resources:
            print(f"Money: $0")
        continue
    elif order == "espresso":
        if check_water(order) == False and check_coffee(order) == False:
            print("Sorry there is not enough water and coffee.")
            running = False
            continue
        elif check_water(order) == False:
            print("Sorry there is not enough water")
            running = False
            continue
        elif check_coffee(order) == False:
            print("Sorry there is not enough coffee")
            running = False
            continue
    elif order == "latte" or order == "cappuccino":
        if check_water(order) == False and check_coffee(order) == False and check_milk(order) == False:
            print("Sorry there is not enough water, coffee, and milk.")
            running = False
            continue
        elif check_water(order) == False and check_coffee(order) == False:
            print("Sorry there is not enough water and coffee.")
            running = False
            continue
        elif check_water(order) == False and check_milk(order) == False:
            print("Sorry there is not enough water and milk.")
            running = False
            continue
        elif check_milk(order) == False and check_coffee(order) == False:
            print("Sorry there is not enough milk and coffee.")
            running = False
            continue
        elif check_water(order) == False:
            print("Sorry there is not enough water")
            running = False
            continue
        elif check_coffee(order) == False:
            print("Sorry there is not enough coffee")
            running = False
            continue
        elif check_milk(order) == False:
            print("Sorry there is not enough milk")
            running = False
            continue

    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickels = float(input("How many nickels?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01

    total = quarters + dimes + nickels + pennies
    if total < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        running = False
        continue

    change = total - MENU[order]["cost"]
    if "money" in resources:
        resources["money"] += MENU[order]["cost"]
    else:
        resources["money"] = MENU[order]["cost"]

    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    resources["water"] -= MENU[order]["ingredients"]["water"]
    if order == "latte" or order == "cappuccino":
        resources["milk"] -= MENU[order]["ingredients"]["milk"]

    print(f"Here is ${change:.2f} in change.")
    print(f"Here is your {order} Enjoy!")
