# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date:4/22/23
# Project #: M11
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import csv  # import csv to read and write to csv file
FILENAME = "contacts.csv"  # declaring the csv file to use as FILENAME


def display_title():  # define display title function
    """displays title
    """
    print("Derek Haskell's Contact Manager App")  # app title
    print()


def display_menu():  # define display menu function
    """displays the command menu
    """
    print('COMMAND MENU')  # title
    print()
    print('list - Display all contacts')  # list command
    print('view - View a contact')  # view command
    print('add - Add a contact')  # add command
    print('del - Delete a contact')  # del command
    print('exit - Exit program')  # exit command
    print()


def read_contacts():  # define read contacts function
    """reads from csv file and writes to contacts list

    Returns:
        list: contacts
    """
    contacts = []  # setting contacts to empty list
    try:  # try to open the file
        with open(FILENAME, newline="") as file:  # opens file with with so it closes after
            reader = csv.reader(file)  # reader is csv reader
            for row in reader:  # loop through rows
                contacts.append(row)  # append each row to contacts list
        return contacts  # return the contacts list

    except FileNotFoundError:  # for specific error
        # prints message specific to error
        print('Could not find contacts file! Starting new contacts file...')
        return contacts  # returns the contacts list


def display(contacts):  # define display function with contacts as parameter
    """displays contact

    Args:
        contacts (list): information
    """
    if len(contacts) == 0:  # checks is length of contacs is zero
        # displays if no contacts are in the list
        print("There are no contacts in the list")
        return  # returns
    else:  # if
        # enumerates the contacts list starting at one to number the list
        for i, row in enumerate(contacts, start=1):
            print(f"{i}. {row[0]}")  # prints list with different fields
        print()


def get_contact_number(contacts):  # define get contact number function
    """gets contact number 

    Args:
        contacts (list): int

    Returns:
        int: greater than zero
    """
    while True:  # start infinate while loop
        try:  # tries input to check for exceptions
            number = int(input("Number: "))  # number is int input of user
        except ValueError:  # checks for a specific error
            print("Invalid integer.\n")  # invalid message
            return -1  # returns last

        if number < 1 or number > len(contacts):  # checks for valid input
            print("Invalid contact number.\n")  # invalid message
            return -1  # returns last
        else:  # if valid input
            return number  # returns number if valid


def add(contacts):  # define add function receiving contacts as a parameter
    """adds contacts

    Args:
        contacts (list): name,email,phone as input
    """

    name = input("Name: ")  # get user input for name
    email = input("Email: ")  # get user input for email
    phone = input("Phone: ")  # get user input for phone number
    contact = []  # setting contact to empty list
    contact.append(name)  # appends name to contact
    contact.append(email)  # appends email to contact
    contact.append(phone)  # appends phone to contact
    contacts.append(contact)  # appends contact to contacts
    write_contacts(contacts)  # calls write contacts function
    # prints with different fields and variables
    print(f"{contact[0]} was added.")
    print()


def write_contacts(contacts):  # define write contacts function
    """opens csv file in write mode

    Args:
        contacts (list): writes to list from csv file
    """
    with open(FILENAME, "w", newline="") as file:  # opens csv file with with open in write mode
        writer = csv.writer(file)  # sets writer to write calls csv from module
        writer.writerows(contacts)  # writes rows to contacts


def delete(contacts):  # define delete function that receives contacts list as a parameter
    """deletes a contact

    Args:
        contacts (list): deletes contact from the correct index
    """
    number = get_contact_number(
        contacts)  # calls get contacts number function and sets equal to number
    if number > 0:  # checks if number is greater than zero
        # deletes contact from contacts at the correct index after if subracts one
        contact = contacts.pop(number-1)
        print(f"{contact[0]} was deleted.\n")  # print different fields
    # calls write contacts function to write the new rows to the contacts list
    write_contacts(contacts)


def view(contacts):  # define a view function that recieves contacts as a parameter
    """view a contact

    Args:
        contacts (list): view a single contact
    """

    # calls get contact number function sets value to number
    number = get_contact_number(contacts)

    if number > 0:  # makes sure number is greater than zero then
        contact = contacts[number-1]  # setting to correct index
        print("Name:", contact[0])  # display name
        print("Email:", contact[1])  # display email
        print("Phone:", contact[2])  # display phone
        print()


def main():  # define main function
    """main function the app
    """
    contacts = read_contacts()  # calls read contact function sets to contacts as list
    display_title()  # calls display title function
    display_menu()  # calls display menu function
    while True:  # starts infinate loop for command input from user
        command = input("Command: ")  # get input from user for command
        if command == "list":  # if input is list
            display(contacts)  # displays all contacts
        elif command == "view":  # if command is view
            view(contacts)  # views a contact
        elif command == "add":  # if command is add
            add(contacts)  # adds a contact
        elif command == "del":  # if command is del
            delete(contacts)  # deletes contact
        elif command == "exit":  # if command is exit
            break  # breaks out of loop or exits
        else:  # if invalid command
            print("Not a valid command. Please try again.\n")  # invalid message
    print("Bye!")  # goodbye message


if __name__ == "__main__":  # checks if there is a main
    main()  # runs main as main
