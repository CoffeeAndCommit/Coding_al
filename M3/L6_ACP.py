# Assignment: Months
# Write a program to display all the month’s names.

import calendar

print("All the Month's Names:")
# calendar.month_name contains month names, starting with an empty string at index 0
for month in list(calendar.month_name)[1:]:
    print(month)
