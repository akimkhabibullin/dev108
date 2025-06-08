# Assignment Title: Old MacDonald Rhyme
# Class: Dev108
# Date: 5, 24, 25
# Your Name: Akim Khabibullin
# Assignment Description: A program to print the lyrics of "Old MacDonald"using functions to avoid code duplication


# Define the repeated lines as constants
FARM_LINE = "Old MacDonald had a farm"
EE_LINE = "Ee i ee i o"

def printRefrain():
    # Prints the repeated refrain lines
    print(FARM_LINE)
    print(EE_LINE)

def printVerse(animal, sound):
    # Prints a full verse for a specific animal and sound
    printRefrain()
    print(f"And on his farm he had some {animal}")
    print(EE_LINE)
    print(f"With a {sound}-{sound} here")
    print(f"And a {sound}-{sound} there")
    print(f"Here a {sound}, there a {sound}")
    print(f"Everywhere a {sound}-{sound}")
    printRefrain()

def main():
    # Main function, organizes and prints all verses
    printVerse("cows", "moo")
    print()
    printVerse("chicks", "cluck")
    print()
    printVerse("ducks", "quack")

# Call the main function to run teh program
main()
