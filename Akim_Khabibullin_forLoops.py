# Name: Akim Khabibullin
# Date: 5/13/25
# class: Dev 108
# Assignment: Simple Pattern Generator

print("Welcome to pattern generator")

# Get size from user and makes sure its valid
while True:
    size = int(input("Please enter the size (odd number 7-15): "))
    if 7 <= size <= 15 and size % 2 == 1:
        break
    print("Size must be an odd number between 7 and 15")

# Pattern 1 with the symbols
print(f"\nPattern 1 of size {size}")
for i in range(size):
    slashes = "\\" * (2*i)
    dollars = "$" * (size - i)
    stars = "*" * (2*(size - i) - 1)
    print(slashes + dollars + stars + dollars + slashes.replace("\\", "/"))

# Pattern 2 with the Mirror A's
print(f"\nMirror image pattern of size {size}")
# Top part of it
for i in range(1, size + 1):
    a = "A" * i
    space = " " * (2*(size - i) - 1)
    if i == size:
        print("A" * (2*size - 1))  # for middle line
    else:
        print(a + space + a)

# Bottom part
for i in range(size - 1, 0, -1):
    a = "A" * i
    space = " " * (2*(size - i) - 1)
    print(a + space + a)

print("Bye")
