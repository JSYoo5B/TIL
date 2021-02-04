#!/usr/bin/env python3
""" Brute-force solution
Calculate through the rules of calander
"""

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return True

if __name__ == '__main__':
    days_in_month = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_leap = days_in_month.copy()
    days_in_month_leap[2] = 29

    # Remain only days
    diff_in_month = [d % 7 for d in days_in_month]
    diff_in_month_leap = [d % 7 for d in days_in_month_leap]
    # 1 Jan 1900 was a Monday
    first_days = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for m in range(2, 12+1):
        first_days[m] = (first_days[m-1] + diff_in_month[m-1]) % 7
    first_days[0] = first_days[12]

    # Loop for each years
    month_starts_sun = 0
    for y in range(1901, 2001):
        for m in range(1, 12+1):
            if is_leap_year(y):
                first_days[m] = (first_days[m-1] + diff_in_month_leap[m-1]) % 7
            else:
                first_days[m] = (first_days[m-1] + diff_in_month[m-1]) % 7
        first_days[0] = first_days[12]
        month_starts_sun += first_days[0:12].count(0)
 
    print(month_starts_sun)

