
print("Welcome to the Babysitter Payment Calculator")
total = 0.0

keep_going = True
while keep_going:
    rate = float(input("\nEnter the hourly rate: "))
    hours = int(input("Enter the number of hours worked: "))
    
    if hours <= 5:
        pay = hours * rate
    elif hours <= 8:
        pay = (5 * rate) + ((hours - 5) * rate * 0.8)
    else:
        pay = (5 * rate) + (3 * rate * 0.8) + ((hours - 8) * rate * 0.5)
    
    total = total + pay
    print(f"Daily pay: ${pay:.2f} Total pay so far: ${total:.2f}")
    
    answer = input("Do you want to enter more data? (y/Y to continue): ")
    if answer.lower() != "y":
        keep_going = False

print(f"\nFinal total payment: ${total:.2f}")
print("Bye")
