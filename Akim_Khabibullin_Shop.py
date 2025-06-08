# Coffee Shop Cost Calculator
# Class: DEV108
# Section: 10723
# Date: 4/21/25
# Name: Akim Khabibullin
# Description: This program generates a statement for AK Coffee Shop
# It asks for date and coffee amount, then calculates cost, shipping, tax, and total for three days

print("*" * 60)
print("Welcome to AK Coffee Shop")  
print("*" * 60)

# Initials AK
print("        A            K   K  ")
print("       A A           K  K   ")
print("      A   A          K K    ")
print("     AAAAAAA         KK     ")
print("    A       A        K K    ")
print("   A         A       K  K   ")
print("  A           A      K   K  ")

# Get user input
day = int(input("Please enter date of the month: "))
pounds = int(input("Please enter the amount of coffee in pounds: "))

print("*" * 60)

# Constants
pricepound = 7.50
cost = pricepound * pounds
shipping = round(0.85 * pounds + 4.50, 2)

print("Shipping cost:", shipping)
print("-" * 60)

# Table header
print("Date  | Cost   | Tax   | Total (Cost + Shipping + Tax)")
print("-" * 60)

# Loop through today, tomorrow, and day after
for offset in range(3):
    current_day = day + offset
    if current_day > 31:
        current_day -= 31

    # Tax rate calculation per assignment rule
    days_left = 31 - current_day
    tax_rate = days_left / 5
    tax_rate /= 100  # compound assignment used here

    tax_amount = round(cost * tax_rate, 2)
    total = round(cost + shipping + tax_amount, 2)

    # end parameter used here
    print(f"{current_day:<6} | {cost:<7.2f}| {tax_amount:<6.2f}| ", end="")
    print(f"{total:.2f}")

print("-" * 60)
print("Bye")
