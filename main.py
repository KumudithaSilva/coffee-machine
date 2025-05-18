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

coins = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies": 0.01
}

cash = 0
machineState = True

# TODO : 1. Print report of all coffee machine resources
def resources_details(resource_details, money):
    return (f"===Detailed Report===\n"
            f"Water: {resource_details['water']}ml\n"
            f"Milk: {resource_details['milk']}ml\n"
            f"Coffee: {resource_details['coffee']}g\n"
            f"Money: ${money}\n{'='*20}\n")

# TODO : 2. Check resources sufficient to make drink water
def calculate_resources(userchoices):
    ingredients = MENU[userchoices]['ingredients']
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.\n")
            return False
    return True

# TODO : 5. Process coins.
def process_coin():
    total = 0
    for item  in coins:
        user_coin = int(input(f"How many {item}:"))
        total += user_coin * coins[item]
    print(f"\nTotal is ${total}")
    return total

# TODO : 6. Check transaction successful?
def transaction(user_total, coffe_cost, cash_amount):
    global cash
    if coffe_cost > user_total:
        print("Sorry that's not enough money. Money refunded.\n")
        return False
    else:
        if user_total >= coffe_cost:
            print(f"Here is ${round(user_total-coffe_cost, 2)} dollars in change.\n")
        cash = cash_amount + coffe_cost
        return True

# TODO : 7. Make Coffee.
def make_coffe(userchoices):
    ingredients = MENU[userchoices]['ingredients']
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {userchoices}. Enjoy!\n")

# TODO : 3. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
# TODO : 4. Turn off the Coffee Machine by entering “ off ” to the prompt.
print(resources_details(resources, cash))
while machineState:
    userinput = input("What would you like? (espresso/latte/cappuccino):")
    if userinput == "off":
        machineState = False
    elif userinput == "report":
        print(resources_details(resources, cash))
    elif userinput in  {"espresso", "latte", "cappuccino" }:
        if calculate_resources(userinput):
            coffe_price = MENU[userinput]['cost']
            print(f"\nTotal amount for the {userinput} is ${coffe_price}")
            user_amount = process_coin()
            if transaction(user_amount, coffe_price, cash):
                make_coffe(userinput)
    else:
        print("Invalid input. Please choose correct commands.")
    print(resources_details(resources, cash))






























