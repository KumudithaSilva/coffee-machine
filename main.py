from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machineState = True
print(f"===Detailed Report===")
coffee_maker.report()
money_machine.report()
while machineState:
    options = menu.get_items()
    userinput = input(f"What would you like? ({options}): ")
    if userinput == "off":
        machineState = False
    elif userinput == "report":
        print(f"===Resource Report===")
        coffee_maker.report()
        money_machine.report()
    elif userinput in {"espresso", "latte", "cappuccino"}:
        drink = menu.find_drink(userinput)
        if coffee_maker.is_resource_sufficient(drink):
            coffe_price = menu.find_drink(userinput).cost
            print(f"\nTotal amount for the {userinput} is ${coffe_price}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("Invalid input. Please choose correct commands.")
































