# Name: (First Name Last Name)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date:4/1/23
# Project #: M09
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

def main():  # main function defined
    """
    main function runs all other functions
    """
    display_title()  # run display_title function
    display_menu()  # run display_menu function

    # creating default list items carried
    inventory = ["potion", "dagger", "cloak"]
    while True:  # start infinate loop
        command = input("Command: ")  # geet user input command
        if command == "show":  # if user types show
            show(inventory)  # calls show function
        elif command == "grab":  # if user types grab
            grab_item(inventory)  # calls grab_item function
        elif command == "edit":  # if user types edit
            edit_item(inventory)  # calls edit_item function
        elif command == "drop":  # if user types drop
            drop_item(inventory)  # calls drop_item function
        elif command == "exit":  # if user types exit
            break  # breaks while loop
        else:
            # if command is invalid invalid message
            print("Not a valid command. Please try again.\n")
    print("Bye!")  # goodbye message


def display_title():  # display_title function defined
    """
    Game Title
    """
    print("Derek Haskell's Wizard Inventory Game")  # display title
    print()


def display_menu():  # display menu function defined
    """
    displays command menu
    """
    print("show - Show all items")  # prints display menu to console
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")


def show(inventory):  # show inventory defined
    """
    shows inventory

    Args:
        inventory (list): items
    """
    for number, item in enumerate(inventory, start=1):  # format list with numbers
        print(f"{number}. {item}")  # shows inventory


def grab_item(inventory):  # grab_item function defined
    """adds item

    Args:
        inventory (list): item
    """
    if len(inventory) >= 4:  # check if inventory is full
        # too many items message
        print("You can't carry any more items. Drop something first.\n")
    else:  # if room for new items
        item = input("Name: ")  # get user input
        inventory.append(item)  # append inventory list
        print(f"{item} was added.\n")  # let user know their item was added


def edit_item(inventory):  # edit_item function defined
    """
    edits item

    Args:
        inventory (list): item
    """
    number = int(input("Number: "))  # get user input convert to integer
    if number < 1 or number > len(inventory):  # checks for valid number
        print("Invalid item number.\n")  # invalid number message
    else:  # if valid number
        item = input("Updated name: ")  # get user input
        inventory[number-1] = item  # editing inventory
        # let user know item has been updated
        print(f"Item number {number} was updated.\n")


def drop_item(inventory):  # drop_item function defined
    """
    drops item selects number based off user input
    """
    number = int(input("Number: "))  # convert user input to integer
    if number < 1 or number > len(inventory):  # checks for valid number
        print("Invalid item number.\n")  # invalid number message
    else:  # if valid number
        item = inventory.pop(number-1)  # erase item
        print(f"{item} was dropped.\n")  # let user know item was dropped


if __name__ == "__main__":  # if main function is present run main
    main()
