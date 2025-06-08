# Assignment: Zeller's algorithm
# Class: DEV108
# Date: April 27, 2025
# Author: Akim Khabibullin
# Description: Program to display day of the week for a given date

month = int(input("Enter month: "))
day = int(input("Enter the date: "))
year = int(input("Enter the year: "))

if not (1582 <= year <= 4902) or not (1 <= month <= 12):
    print("Invalid input")
    exit()
    
def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

days_in_month = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

if day < 1 or day > days_in_month[month - 1]:
    print("Invalid date input.")
    exit()

if month < 3:
    month += 12
    year -= 1

a = month - 2
b = day
c = year % 100
d = year // 100

print(f"a b c d = {a} {b} {c} {d}")

w = (13 * a - 1) // 5
x = c // 4
y = d // 4
z = w + x + y + b + c - 2 * d
r = z % 7
r = (r + 7) % 7  

print(f"w x y z r = {w} {x} {y} {z} {r}")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"Day of the week: {days[r]}")
