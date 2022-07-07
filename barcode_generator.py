import turtle
from digitprint import *

# Ends program 
def t_end():
    turtle.done()
    try:
        turtle.bye()
    except:
        print("Program Complete") 

# Creates large line for barcode
def big_line(myTurtle):
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.forward(4)
    myTurtle.right(90)
    myTurtle.forward(50)
    space_line(t)

# Creates small line for barcode
def small_line(myTurtle):
    myTurtle.left(90)
    myTurtle.forward(20)
    myTurtle.right(90)
    myTurtle.forward(4)
    myTurtle.right(90)
    myTurtle.forward(20)
    space_line(t)
 
# Creates a space between big_line and small_line
def space_line(myTurtle):
    myTurtle.left(90)
    myTurtle.forward(3)

# Prints a big_line() for the start and end of the barcode
def print_startstop(myTurtle):
    big_line(t)
 
# prints barcode number
def print_zero(myTurtle):
    for i in range(2):
        big_line(t)
    for i in range(3):
        small_line(t)

def print_one(myTurtle):
    for i in range(3):
        small_line(t)
    for i in range(2):
        big_line(t)

def print_two(myTurtle):
    for i in range(2):
        small_line(t)
    big_line(t)
    small_line(t)
    big_line(t)

def print_three(myTurtle):
    for i in range(2):
        small_line(t)
    for i in range(2):
        big_line(t)
    small_line(t)

def print_four(myTurtle):
    small_line(t)
    big_line(t)
    for i in range(2):
        small_line(t)
    big_line(t)

def print_five(myTurtle):
    small_line(t)
    big_line(t)
    small_line(t)
    big_line(t)
    small_line(t)

def print_six(myTurtle):
    small_line(t)
    for i in range(2):
        big_line(t)
    for i in range(2):
        small_line(t)

def print_seven(myTurtle):
    big_line(t)
    for i in range(3):
        small_line(t)
    big_line(t)

def print_eight(myTurtle):
    big_line(t)
    for i in range(2):
        small_line(t)
    big_line(t)
    small_line(t)

def print_nine(myTurtle):
    big_line(t)
    small_line(t)
    big_line(t)
    for i in range(2):
        small_line(t)

# Creates a solid line underneath the completed barcode
def finish_line(myTurtle):
    myTurtle.left(180)
    myTurtle.forward(46*8)
 
# Calculates the last digit of the barcode
def checksum(array_string):
    total = 0
    for i in array_string:
        if i == '-':
            continue
        i = int(i)
        total = total + i
    check = 10 - (total % 10)
    return check 

# Function generates barcode
def generate_barcode(list_of_strnums):
    for i in list_of_strnums:
        if i == '1':
            print_one(t)
        elif i == '2':
            print_two(t)
        elif i == '3':
            print_three(t)
        elif i == '4':
            print_four(t)
        elif i == '5':
            print_five(t)
        elif i == '6':
            print_six(t)
        elif i == '7':
            print_seven(t)
        elif i == '8':
            print_eight(t)
        elif i == '9':
            print_nine(t)
        elif i == '0':
            print_zero(t)
        elif i == '-':
            continue
        else:
            break

# function generates the last digit of the barcode
def generate_checksum(check):
    if check == 1:
        print_one(t)
    elif check == 2:
        print_two(t)
    elif check == 3:
        print_three(t)
    elif check == 4:
        print_four(t)
    elif check == 5:
        print_five(t)
    elif check == 6:
        print_six(t)
    elif check == 7:
        print_seven(t)
    elif check == 8:
        print_eight(t)
    elif check == 9:
        print_nine(t)
    elif check == 0:
        print_zero(t)
    else:
        print_zero(t)

# checks if barcode is valid
def string_check():
    while True:
        flag = 2
        length_checker = 0   
        zipcode = input("Please input zipcode (ex. 55555-1234): ")
        split_string = list(zipcode)
        for i in split_string:
            if i == '1' or i == '2' or i == '3' or i == '4' or i =='5' or i =='6' or i =='7' or i =='8' or i =='9' or i =='0' or i == '-':
                continue
            else:
                flag = flag - 1
                print("Unrecognized character. Try again.")
                break
        for i in range(0, len(split_string)):
            length_checker = length_checker + 1
        if length_checker != 10:
            flag = flag - 1
            print("Invalid length. Try again.")
        if flag == 2:
            print("--GENERATING BARCODE--")
            return split_string

def main():
    splitstr = string_check()
    check_sum = checksum(splitstr)
    t.fillcolor('black')
    t.begin_fill()
    
    print_startstop(t)
    generate_barcode(splitstr)
    generate_checksum(check_sum)
    print_startstop(t)
    
    finish_line(t)
    t.end_fill()
    t_end()

t = turtle.Turtle()
main()
