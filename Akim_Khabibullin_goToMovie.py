print("Welcome to the movie program.")

price = float(input("Enter the ticket price: "))
while price < 0:
    print("Price cannot be negative.")
    price = float(input("Enter the ticket price: "))

stars = int(input("Enter the number of stars: "))
while stars < 1 or stars > 5:
    print("Number of stars cannot be less than 1 or greater than 5.")
    stars = int(input("Enter the number of stars: "))

if price < 5:
    decision = "Yup"
elif price >= 12:
    decision = "Maybe" if stars == 5 else "Nope"
else:
    decision = "Yup" if stars == 5 else "Maybe"

print(f"Will you go to the movie? {decision}")
