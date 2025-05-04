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
    },
    "americano": {
        "ingredients":{
            "water": 250,
            "milk": 0,
            "coffee":30
        },
        "cost" : 2.5
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True

def process_coin():
    print(("Insert coin: "))
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_succesful(money_recieve, drink_cost):
    if money_recieve >= drink_cost:
        change = round(money_recieve - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money, money refunded")
        return False
    
def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. enjoy")

is_on = True

while is_on:
    choice = (input("Plese chose your drink (Espresso/Latte/Cappucino/Americano)")) 
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(F"Water {resources['water']}")
        print(F"Milk {resources['milk']}")
        print(F"coffe {resources['coffee']}")
        print(F"money {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"]) 
