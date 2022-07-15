def calculator():
    try:
        first_num = int(input("What is your first number? "))
        operation(first_num)
    except ValueError:
        print("Invalid entry. Try again")
        calculator()

def operation(first):
    operation_helper_list = ['+', '-', '*', '/']
    valid_operations = ' '.join(operation_helper_list)
    print("Valid operations: {}".format(valid_operations))
    while True:
        operation = input("Pick an operation: ")
        if operation not in operation_helper_list:
            print("Please input a proper operation.")
        else:
            break
    try:
        second = int(input("What's the next number? "))
        total = 0
        if operation == "+":
            total = round(addition(first, second),2)
            print("{} + {} = {}".format(first, second, total))
            num1 = total
        if operation == '-':
            total = round(subtraction(first, second),2)
            print("{} - {} = {}".format(first, second, total))
            num1 = total
        if operation == '*':
            total = round(multiplication(first, second),2)
            print("{} * {} = {}".format(first, second, total))
            num1 = total
        if operation == '/':
            total = round(division(first, second),2)
            print("{} / {} = {}".format(first, second, total))
            num1 = total
    except:
        print("Something went wrong. Try again")
        calculator()

    while True:
        print("Type 'y' to use calculator again".format(total))
        print("Type 'n' to exit")
        choice = input("Please type 'y' or 'n': ").lower()
        if choice == 'y':
            calculator()
        elif choice == 'n':
            return
        else:
            print("Please input 'y' or 'n'")

def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

def main():
    calculator()

if __name__ == '__main__':
    main()
