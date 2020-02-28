import math


def if_leap_year(year):
    if year % 4 != 0:
        return "common year"
    elif year % 4 == 0 and year % 100 != 0:
        return "leap year"
    elif year % 100 == 0 and year % 400 != 0:
        return "common year"
    elif year % 400 == 0 and year % 3200 != 0:
        return "leap year"
    else:
        return "common year"


def get_day_of_the_week(year, month, day_of_month):
    if month == 1 or month == 2:
        month += 12
        year -= 1
    q = day_of_month
    m = month
    k = year % 100
    j = math.floor(year / 100)
    h = (q + math.floor(13 * (m + 1) / 5) + k + math.floor(k / 4) + math.floor(j / 4) - 2 * j) % 7
    d = ((h + 5) % 7) + 1
    return d


get_day_of_the_week(2019, 2, 5)


# 今天星期几
# today = int(time.strftime("%w"))

# 某个日期星期几


def generate_blank_list(number):
    blank_list = []
    for x in range(number):
        blank_list.append('  ')
    return blank_list


print('*********************************************')


def print_heading(input_year, input_month):
    input_month = int(input_month)
    if input_month > 12 or input_month < 0:
        print('please enter valid month')

    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_name = month_list[input_month - 1]
    print('\t\t' + month_name + '\t' + str(input_year))
    i = 5

    print('Mon\tTue\tWed\tThu\tFri\tSat\tSun')


def print_calendar_body(input_year, input_month):
    input_year = int(input_year)
    input_month = int(input_month)

    first_day = get_day_of_the_week(input_year, input_month, 1)
    print('\t' * (first_day - 1), end='')
    days_of_month = determine_days_of_month(input_year, input_month)

    for i in range(1, days_of_month + 1):
        print(i, end='\t')
        if get_day_of_the_week(input_year, input_month, i) == 7:
            print('', end='\n')


def determine_days_of_month(input_year, input_month):
    days_of_month = 0
    if input_month in {1, 3, 5, 7, 8, 10, 12}:
        days_of_month = 31
    elif input_month in {4, 6, 9, 11}:
        days_of_month = 30
    elif input_month == 2:
        if if_leap_year(input_year) == 'leap year':
            days_of_month = 29
        else:
            days_of_month = 28

    return days_of_month


def print_calendar(input_year, input_month):
    print_heading(input_year, input_month)
    print_calendar_body(input_year, input_month)


print_calendar(2000, 5)
