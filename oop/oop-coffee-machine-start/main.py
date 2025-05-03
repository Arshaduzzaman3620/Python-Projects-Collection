from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
CoffeeMaker = CoffeeMaker()
menu = Menu()
is_on = True 
CoffeeMaker.report()
money_machine.report()

while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? ({options}): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    CoffeeMaker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if CoffeeMaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        
        CoffeeMaker.make_coffee(drink)