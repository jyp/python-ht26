# Problem: How old am I, in number of days?

# Generalisation: What is the number of days between two arbitrary dates?

average_number_of_days_in_a_year = 365.2422
average_number_of_days_in_a_month = average_number_of_days_in_a_year / 12
# Interface.
# inputs: two dates. each 3 numbers: year, month, day.
# output: number of days (as integer) 

def approximate_date_diff(y1,m1,d1, y2,m2,d2):
    return ((y2-y1)*average_number_of_days_in_a_year +
             (m2-m1)*average_number_of_days_in_a_month +
             (d2-d1))

def is_leap_year(year):
    #  Returns true if we have a extra leap day in given year.
    # That is, return true if year  is a multiple of 4, except for years evenly divisible by 100 but not by 400.
    # Source: https://en.wikipedia.org/wiki/Leap_year (20260903)
    if year % 100 == 0 and not (year % 400) == 0:
        return False
    return (year % 4) == 0

assert not is_leap_year(2001)
assert is_leap_year(1600)
assert is_leap_year(2000)
assert not is_leap_year(1700)

def number_of_days_in_year(year):
    if is_leap_year(year):
        return 366
    else:
      return 365
def number_of_days_in_month(month,year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    if month in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30

def date_diff_to_epoch(year,month,day):
    # count the number of days between 1st january 1 and the given date.
    count = 0
    for y in range(year):
        count = count + number_of_days_in_year(y)
    for m in range(month):
        count = count + number_of_days_in_month(m,y)
    count = count + day
    return count

def date_diff(y1,m1,d1, y2,m2,d2):
    return date_diff_to_epoch(y2,m2,d2) - date_diff_to_epoch(y1,m1,d1)

print(date_diff(2026,9,3,  2026,9,3))
print(date_diff(2026,9,3,  2026,10,3))

print(date_diff(1978,12,15,  2026,9,3))
print(approximate_date_diff(1978,12,15,  2026,9,3))

