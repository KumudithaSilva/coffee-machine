from pkg_resources import non_empty_lines

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

cash = 0
machineState = True

# TODO : 4. Turn off the Coffee Machine by entering “ off ” to the prompt.
# TODO : 5. Process coins.
# TODO : 6. Check transaction successful?
# TODO : 7. Make Coffee.

# TODO : 1. Print report of all coffee machine resources

def resources_details(details, money):
    water = details['water']
    milk = details['milk']
    coffee = details['coffee']
    return f"===Detailed Report===\nWater: {water}ml\
    nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}\n{'='*20}"

# TODO : 2. Check resources sufficient to make drink water
# TODO : 3. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):

def calculate_resources(userchoices):
    print(f"{userchoices}")

userinput = input("What would you like? (espresso/latte/cappuccino):")
if userinput == "off":
    machineState = False
elif userinput == "espresso":
    calculate_resources(userinput)
elif userinput == "latte":
    calculate_resources(userinput)
elif userinput == "cappuccino":
    calculate_resources(userinput)






























