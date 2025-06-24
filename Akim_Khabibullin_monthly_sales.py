#!/usr/bin/env python3

# Monthly Sales Program
# Date: 6/22/25
# Your Name: Akim Khabibullin
# Description: this program reads monthly sales data from a file and allows users to view the sales numbers and edit sales for any month.

import csv
import sys
# Constants
FILENAME = "monthly_sales.csv"
MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def read_sales():
    # reads sales data from the months file and returns it as a list of lists
    sales = []  # makes a empty list
    try:
        # open the file to reading throuhg
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # skips empty 
                    month = row[0].strip()
                    # convert sales number to integer and adds to the list
                    sales_figure = int(row[1].strip())
                    sales.append([month, sales_figure])
    except FileNotFoundError:
        # if file is missing stop program
        print(f"Error: Could not find {FILENAME} file.")
        sys.exit(1)
    except Exception as e:
        # if cant read it then also stop 
        print(f"Error reading file: {e}")
        sys.exit(1) 
    return sales

def write_sales(sales):
    # writes sales data back to the  file
    try:
        # open the file for writing
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(sales)  
    except Exception as e:
        # handle file writing errors
        print(f"Error writing to file: {e}")
        sys.exit(1) 

def view_monthly_sales(sales):
    # displays monthly sales data in a formatted list
    for entry in sales:
        month = entry[0]
        amount = entry[1] 
        print(f"{month} - {amount}")  

def edit(sales):
    try:
        # get and validate month input
        month = input("Three-letter Month: ").strip()
        if month not in MONTH_NAMES:
            raise ValueError("Invalid three-letter month.")
        
        # get and validate sales amount
        amount_str = input("Sales Amount: ").strip()
        try:
            amount = int(amount_str)
        except ValueError:
            # handle noninteger input
            raise ValueError("Invalid sales amount. Please enter an integer.")
        
        # update sales data for the month choosen
        for entry in sales:
            if entry[0] == month:
                entry[1] = amount
                break
        
        # save updated data to file
        write_sales(sales)
        # confirm successful update
        print(f"Sales amount for {month} was modified.")
        
    except ValueError as ve:
        # handle validation errors
        print(f"ValueError: {ve}")

def display_menu():
    # displays the command menu options to the user
    print("COMMAND MENU")
    print("monthly - View monthly sales")
    print("edit    - Edit sales for a month")
    print("exit    - Exit program")
    print()

def main():
    # main program 
    print("Monthly Sales program")
    print()
    # read initial data
    sales = read_sales()
    # show command menu
    display_menu()
    # command processing loop
    while True:
        command = input("Command: ").strip().lower()
        # process user commands
        if command == "monthly":
            view_monthly_sales(sales)
        elif command == "edit":
            edit(sales)
        elif command == "exit":
            break  # Exit loop
        else:
            # non valid commands
            print("Not a valid command. Please try again.\n")
    
    # exit msg
    print("Bye!")

# runs main
if __name__ == "__main__":
    main()
