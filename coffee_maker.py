EXPRESSO_PRICE = 2.99
LATTE_PRICE = 4.99
CAPPUCCINO_PRICE = 3.99

EXPRESSO_INGREDIENTS = {
                        'water' : 5,
                        'milk' : 1,
                        'coffee' : 30,
                        }

LATTE_INGREDIENTS = {
                     'water': 10,
                     'milk' : 15,
                     'coffee' : 15,
                    }

CAPPUCCINO_INGREDIENTS = {
                          'water': 15,
                          'milk' : 20,
                          'coffee' : 10,
                          }


def payment(money_in_machine):
    money_in_machine = 0
    print("Please insert coins.")
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01
    while True:
        try:
            num_of_quarters = int(input("How many quarters? "))
            num_of_dimes = int(input("How many dimes? "))
            num_of_nickels = int(input("How many nickels? "))
            num_of_pennies = int(input("How many pennies? "))
            total_quarters = num_of_quarters * quarter
            total_dimes = num_of_dimes * dime
            total_nickel = num_of_nickels * nickel
            total_penny = num_of_pennies * penny
            payment_total = total_quarters + total_dimes + total_nickel + total_penny
            money_in_machine = round((money_in_machine + payment_total),2)
            return money_in_machine
        except ValueError:
            print("Something went wrong.\nPlease try again.")

def price_checker(amount_given, price_of_coffee):
    if amount_given >= price_of_coffee:
        return True
    else:
        return False

def subtract_from_storage(water_vat, milk_vat, coffee_vat, ingredients_dict):
    remaining_water = water_vat - ingredients_dict['water']
    remaining_milk = milk_vat - ingredients_dict['milk']
    remaining_coffee = coffee_vat - ingredients_dict['coffee']
    return remaining_water, remaining_milk, remaining_coffee

def check_if_enough_resources(water_vat, milk_vat, coffee_vat, ingredients_dict):
    if ingredients_dict['water'] > water_vat:
        print("Not enough water")
        return True
    if ingredients_dict['milk'] > milk_vat:
        print("Not enough milk")
        return True
    if ingredients_dict['coffee'] > coffee_vat:
        print("Not enough coffee")
        return True

def coffee_machine():
    water_storage = 100
    milk_storage = 100
    coffee_storage = 100
    money = 0
    while True:
        choice = input("What would you like? (expresso/latte/cappuccino): ")
        if choice == 'expresso':
            a = check_if_enough_resources(water_storage, milk_storage, coffee_storage, EXPRESSO_INGREDIENTS)
            if a:
                continue
        elif choice == 'latte':
            b = check_if_enough_resources(water_storage, milk_storage, coffee_storage, LATTE_INGREDIENTS)
            if b:
                continue
        elif choice == 'cappuccino':
            c = check_if_enough_resources(water_storage, milk_storage, coffee_storage, CAPPUCCINO_INGREDIENTS)
            if c:
                continue

        if choice == "report":
            print("Water: {}ml".format(water_storage))
            print("Milk: {}ml".format(milk_storage))
            print("Coffee: {}ml".format(coffee_storage))
            print("Money in machine: ${}".format(money))
        elif choice == "expresso":
            my_payment = payment(money)
            if price_checker(my_payment, EXPRESSO_PRICE) == True:
                money = money + EXPRESSO_PRICE
                my_change = round((my_payment - EXPRESSO_PRICE), 2)
                print("Returning change: ${}".format(my_change))
                print("Enjoy your expresso!")
                water_storage = subtract_from_storage(water_storage, milk_storage, coffee_storage, EXPRESSO_INGREDIENTS)[0]
                milk_storage = subtract_from_storage(water_storage, milk_storage, coffee_storage, EXPRESSO_INGREDIENTS)[1]
                coffee_storage = subtract_from_storage(water_storage, milk_storage, coffee_storage, EXPRESSO_INGREDIENTS)[2]
            else:
                print("Not enough money")
                print("Price of expresso: ${}".format(EXPRESSO_PRICE))
                print("Amount given: ${}".format(my_payment))

        elif choice == "latte":
            my_payment = payment(money)
            if price_checker(my_payment, LATTE_PRICE) == True:
                money = money + LATTE_PRICE
                my_change = round((my_payment - LATTE_PRICE), 2)
                print("Returning change: ${}".format(my_change))
                print("Enjoy your latte!")
                water_storage = subtract_from_storage(water_storage, milk_storage, coffee_storage, LATTE_INGREDIENTS)[0]
                milk_storage = subtract_from_storage(water_storage, milk_storage, coffee_storage, LATTE_INGREDIENTS)[1]
                coffee_storage = subtract_from_storage(water_storage, milk_storage, coffee_storage, LATTE_INGREDIENTS)[2]
            else:
                print("Not enough money")
                print("Price of latte: ${}".format(CAPPUCCINO_PRICE))
                print("Amount given: ${}".format(my_payment))
        elif choice == "cappuccino":
            my_payment = payment(money)
            if price_checker(my_payment, CAPPUCCINO_PRICE) == True:
                money = money + CAPPUCCINO_PRICE
                my_change = round((my_payment - CAPPUCCINO_PRICE), 2)
                print("Returning change: ${}".format(my_change))
                print("Enjoy your cappuccino!")
                water_storage = subtract_from_storage(water_storage, milk_storage, coffee_storage, CAPPUCCINO_INGREDIENTS)[0]
                milk_storage = subtract_from_storage(water_storage, milk_storage, coffee_storage, CAPPUCCINO_INGREDIENTS)[1]
                coffee_storage = subtract_from_storage(water_storage, milk_storage, coffee_storage, CAPPUCCINO_INGREDIENTS)[2]
            else:
                print("Not enough money")
                print("Price of cappuccino: ${}".format(CAPPUCCINO_PRICE))
                print("Amount given: ${}".format(my_payment))
        else:
            print("Something went wrong.\nTry again.")

def main():
    coffee_machine()

if __name__ == '__main__':
    main()
