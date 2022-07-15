def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        else:
            if year % 100 == 0:
                return False
            return True

def days_in_month(my_year, my_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(my_year) is True:
        month_days[1] = 29
    return month_days[my_month -1]

def main():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)

    the_months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
                    'Sept','Oct','Nov','Dec']
    print("In the year {}, {} has {} days.".format(year, the_months[month-1], days))

if __name__ == '__main__':
    main()
