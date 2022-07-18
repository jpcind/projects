WATER_STORAGE = 300
MILK_STORAGE = 200
COFFEE_STORAGE = 100
MONEY_IN_MACHINE = 0

class Coffee_Machine:
    def __init__(self, coffee_type:str, price:int, ingredients:dict):
        self.coffee_type = coffee_type
        self.price = price
        self.ingredients = ingredients

    def coffee_information(self):
        print("Coffee type: {}".format(self.coffee_type))
        print("Price: {}".format(self.price))
        print("Ingredients: {}".format(self.ingredients))

    def report(self):
        print("\n-- MACHINE REPORT --")
        print("Water: {}ml".format(WATER_STORAGE))
        print("Milk: {}ml".format(MILK_STORAGE))
        print("Coffee: {}ml".format(COFFEE_STORAGE))
        print("Money in machine: ${}\n".format(MONEY_IN_MACHINE))

    def pay_for_drink(self):
        global MONEY_IN_MACHINE
        global WATER_STORAGE
        global MILK_STORAGE
        global COFFEE_STORAGE
        quarter = 0.25
        dime = 0.10
        nickel = 0.05
        penny = 0.01
        if WATER_STORAGE-self.ingredients['water'] < 0 or MILK_STORAGE-self.ingredients['milk'] < 0 or COFFEE_STORAGE-self.ingredients['coffee'] < 0:
            print("Not enough resources to make {}\n".format(self.coffee_type))
            return False
        print("\nPrice of {}: ${}".format(self.coffee_type, self.price))
        while True:
            try:
                print("Insert coins")
                num_of_quarters = int(input("Quarters: "))
                num_of_dimes = int(input("Dimes: "))
                num_of_nickels = int(input("Nickels: "))
                num_of_pennies = int(input("Pennies: "))
                total_quarters = num_of_quarters * quarter
                total_dimes = num_of_dimes * dime
                total_nickel = num_of_nickels * nickel
                total_penny = num_of_pennies * penny
                payment_total = total_quarters + total_dimes + total_nickel + total_penny
                payment_total = round(payment_total, 2)
                print("Your payment: ${}".format(payment_total))
                if payment_total >= self.price:
                    MONEY_IN_MACHINE += self.price
                    change_return = round(payment_total - self.price, 2)
                    print("Your change is ${}".format(change_return))
                    WATER_STORAGE -= self.ingredients['water']
                    MILK_STORAGE -= self.ingredients['milk']
                    COFFEE_STORAGE -= self.ingredients['coffee']
                    print("Enjoy your {}!\n".format(self.coffee_type))
                    return True
                else:
                    print("Not enough money.\nTry again?")
                    choice = input("Please press 'y' or 'n': ").lower()
                    if choice == 'y':
                        continue
                    elif choice == 'n':
                        print("Bye\n")
                        return
                    else:
                        print("Invalid response. Good bye")
                        return
            except ValueError:
                print("Invalid. Please input number of coins")

def main():
    expresso = Coffee_Machine("expresso", 2.99, {'water':5, 'milk':1, 'coffee':30})
    latte = Coffee_Machine("latte", 4.99, {'water':10, 'milk':15, 'coffee':15})
    cappuccino = Coffee_Machine("cappuccino", 3.99, {'water':15, 'milk':20, 'coffee':10})
    report = Coffee_Machine("NONE", 0, {"NONE":0})

    print("Welcome to J's coffee machine! ")

    while True:
        drink_choice = input("What would you like to drink?\nExpresso, Latte, or Cappuccino?\nEnter 'exit' to leave\n").lower()
        if drink_choice == "expresso":
            if expresso.pay_for_drink() == False:
                continue
        elif drink_choice == "latte":
            if latte.pay_for_drink() == False:
                continue
        elif drink_choice == "cappuccino":
            if cappuccino.pay_for_drink() == False:
                continue
        elif drink_choice == "report":
            report.report()
        elif drink_choice == "exit":
            print("Thank you and good bye!")
            return
        else:
            print("Invalid response. Try again.")

if __name__ == '__main__':
    main()
