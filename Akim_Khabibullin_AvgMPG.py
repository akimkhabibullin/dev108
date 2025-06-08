print("Welcome to the Average MPG Calculator")

start_odometer = float(input("Please enter the starting odometer reading in miles: "))
while start_odometer <= 0:
    start_odometer = float(input("Please enter a positive starting odometer reading: "))

# vars
last_odometer = start_odometer
total_miles = 0
total_fuel = 0
leg_number = 1
more_input = "y"

# Loop for each leg 
while more_input == "y":
    print("--------------------------------------------------------")
    new_odometer = float(input("Please enter new odometer reading in miles for leg #" + str(leg_number) + ": "))
    fuel = float(input("Please enter fuel consumed in gallons for leg #" + str(leg_number) + ": "))

    if new_odometer > last_odometer and fuel > 0:
        miles = new_odometer - last_odometer
        mpg = miles / fuel
        print("MPG for leg #" + str(leg_number) + " = ", mpg)
        total_miles += miles
        total_fuel += fuel
        last_odometer = new_odometer
        leg_number += 1
    else:
        print("Fuel needs to be positive and odometer must be greater than last reading.")

    more_input = input("Continue (y/n)? ")

# display
print("--------------------------------------------------------")
print("Total number of legs in the journey:", leg_number - 1)
if total_fuel > 0:
    avg_mpg = total_miles / total_fuel
    print("Final average MPG for the entire journey:", avg_mpg)
else:
    print("No valid legs entered.")
print("Bye!")
