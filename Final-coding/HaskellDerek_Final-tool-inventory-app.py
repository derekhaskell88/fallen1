#!/usr/bin/env python3
# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date:5/1/23
# Project #: Final Coding
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import csv  # import csv module
FILENAME = "mytools.csv"  # setting filename variable for name of csv file


def main():  # define main function
    """main function runs the infinate command loop"""
    tools = []  # setting tools equal to an empty list
    tools = read_inventory()  # call read inventory function and set tools equal to function
    welcome_message()  # calls welcome message function
    display_menu()  # calls display menu function
    while True:  # start infinate while loop
        command = input("Enter Command-->")  # get user input for command
        command = command.lower()  # converting input to lowercase
        if command == "view":  # checks if command is view
            # calls view inventory function with tools as argument
            view_inventory(tools)
        elif command == "del":  # check if command is del
            # calls delete item function with tools as argument
            delete_item(tools)
        elif command == "add":  # check if command is add
            add_item(tools)  # calls add item function with tools as argument
        elif command == "price":  # check if command is price
            # calls edit price function with tools as argument
            edit_price(tools)
        elif command == "value":  # check if command is value
            # calls total value function with tools as argument
            total_value(tools)
        elif command == "exit":  # check if command is exit
            break  # breaks out of main command loop
        else:  # check if valid command
            print("You must enter a valid command")  # invalid command message
    print("Thank you for using my App!")  # goodbye message


def welcome_message():  # define welcome message function
    """displays message"""
    print("Welcome to Derek Haskell's Tool Inventory App\n")  # print welcome message


def display_menu():  # define display menu function
    """displays command menu"""
    # prints and displays command menu
    print("COMMAND MENU")
    print()
    print("view - View Inventory")
    print("del - Delete Item")
    print("add - Add Item")
    print("price - Edit Price")
    print("value - Inventory Value")
    print("exit - Exit App")
    print()


def read_inventory():  # define read inventory function
    """reads csv file and appends rows to tools list"""
    tools = []  # settingn tools equal to an empty list
    with open(FILENAME, newline="") as file:  # open file with open
        reader = csv.reader(file)  # setting reader equal to csv module reader
        for row in reader:  # loop through rows in csv file
            # append the rows of the csv file to the tools list
            tools.append(row)
    return tools  # return tools list


def view_inventory(tools):  # define view inventory function
    """receives tools as argument and prints tools list """
    print("  Item - Price - Quantity\n")  # columns
    # using a for loop to loop through a 2d list
    for number, row in enumerate(tools, start=1):
        # print rows and items to console
        print(f"{number}-{row[0]} - {row[1]} - {row[2]}")
        print()


def delete_item(tools):  # define delete item function
    """receives tools as argument
    removes item from list"""
    while True:  # start infinate loop for validation
        try:  # start try statement
            remove = int(input("Enter Row Number-->"))  # get user input
        except Exception as e:  # check for valid int
            print(e, "must enter integer")  # invalid message
            continue  # continue back to top of loop
        if remove < 1 or remove > 6:  # checks for valid range
            print("number must be between 1 and 6")  # invalid message
            continue  # continue to top of loop
        else:  # if valid input
            remove = remove-1  # correcting list placement
            # subracting one from quantity of inventory
            tools[remove][2] = int(tools[remove][2])-1
            write_inventory(tools)  # write to csv file
            break  # break out of infinate


def write_inventory(tools):  # define write inventory function with tools as argument
    """writes to csv file"""
    with open(FILENAME, "w", newline="") as file:  # open file with open
        writer = csv.writer(file)  # setting csv writer equal to writer
        writer.writerows(tools)  # write rows to csv file


def add_item(tools):  # define add item function
    """adds item to inventory, receives tools as argument and writes to csv file"""
    while True:  # start infinate loop
        try:  # start try statement
            add = int(input("Enter Row Number-->"))  # get user input
        except Exception as e:  # checks for exception
            print(e, "must enter integer")  # displays exception message
            continue  # continue to top of loop
        if add < 1 or add > 6:  # checks for valid range
            print("number must be between 1 and 6")  # invalid range message
            continue  # top of loop
        else:  # if valid input
            add = add-1  # correct list placement
            tools[add][2] = int(tools[add][2])+1  # add item to list
            write_inventory(tools)  # calls write inventory function
            break  # breaks out of infinate


def edit_price(tools):  # define edit price function with tools as argument
    """edits price of item in list, checks for valid float and int"""
    while True:  # start infinate loop for validation
        try:  # start try statement
            edit = int(input("Enter Row Nuber-->"))  # get user input
        except Exception as e:  # if not valid int
            print(e, "must enter integer")  # invalid int message
            continue  # top of loop
        if edit < 1 or edit > 6:  # checks for valid range
            print("number must be between 1 and 6")  # invalid range message
            continue  # top of loop
        try:  # start try statement
            # get user input as float
            new_price = float(input("Enter new price-->"))
        except Exception as e:  # checks for float not str
            print(e, "must enter number")  # invalid message
            continue  # top of loop
        if new_price < 20 or new_price > 1000:  # checks for valid range
            # invalid range message
            print("Invalid price range, must be between 20 and 1000")
            continue  # top of loop
        else:  # if valid input
            edit = edit-1  # correct list placement
            tools[edit][1] = new_price  # edit list
            write_inventory(tools)  # write to csv file call function
            break  # breaks out of infinate


def total_value(tools):  # define total value function
    """calculates total value of inventory"""
    worth = (float(tools[0][1])*int(tools[0][2]))+(float(tools[1][1])*int(tools[1][2]))+(float(tools[2][1])*int(tools[2][2])) +\
        (float(tools[3][1])*int(tools[3][2]))+(float(tools[4][1])*int(tools[4]
                                                                      [2]))+(float(tools[5][1])*int(tools[5][2]))  # calculates total
    print("\nYour Inventory is worth $", round(
        worth, 3))  # display total worth round to three decimal places if its possible for that to happen


if __name__ == "__main__":  # if main is present run main function as main
    main()  # call main function
