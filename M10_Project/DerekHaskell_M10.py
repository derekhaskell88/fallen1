# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 4/8/23
# Project #: M10
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
import csv  # import csv module
FILENAME = "monthly_sales.csv"  # declare csv file name


def main():  # define maine function
    """main function is app
    """
    sales = []  # setting sales to an empty list

    display_title()  # calls display title function
    display_menu()  # calls the display menu function
    sales = read_sales()  # calls read sales function setting it to value sales
    while True:  # starting infinate while loop
        command = input("Command: ")  # get user input for command
        if command == "monthly":  # if command is monthly
            view_monthly_sales(sales)  # calls view monthly sales function
        elif command == "yearly":  # if command is yearly
            # calls view yearly summary function with sales as a parameter
            view_yearly_summary(sales)
        elif command == "edit":  # if command is edit
            edit(sales)  # calls edit function receiving sales as a parameter
        elif command == "exit":  # if command is exit
            break  # breaks out of infinate while loop
        else:  # if command is not valid
            print("Not a valid command. Please try again.\n")  # invalid message
    print("Bye!")  # goodbye message


def display_title():  # define display title function
    """displays title
    """
    print("Derek Haskell's Monthly Sales")  # displays title
    print()


def display_menu():  # define display menu function
    """displays command menu
    """
    # display menu
    print("COMMAND MENU")  # title
    print()
    print("monthly - View monthly sales")  # monthly command
    print("yearly - View yearly summary")  # yearly command
    print("edit - Edit sales for a month")  # edit command
    print("exit - Exit program")  # exit command
    print()


def read_sales():  # define read sales function
    """reads sales from csv file and writes to list

    Returns:
        list: reads from csv file
    """
    sales = []  # set sales to empty list
    # open with with open csv file lol...
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)  # sets reader to csv reader from module
        for row in reader:  # iderates through rows
            sales.append(row)  # appens row to sales list
    return sales  # returns sales list


# define view monthly sales function receiving sales as paramter
def view_monthly_sales(sales):
    """displays monthly sales to console

    Args:
        sales (list): monthly sales
    """

    for row in sales:  # loops through sales once
        print(f"{row[0]} - {row[1]}")  # prints each row as it loops through
        print()


# define view yearly summary function receiving sales as a parameter
def view_yearly_summary(sales):
    """view yearly sales

    Args:
        sales (list): yearly sales
    """
    total = 0  # setting total to value of zero

    for row in sales:  # loops through rows in sales once
        amount = int(row[1])  # setting amount to int as it loops through
        total += amount  # adding amount to total with a compound operator of plus equals

    # get count
    count = len(sales)

    # calculate average
    average = total / count
    average = round(average, 2)

    # format and display the result
    print("Yearly total:    ", total)
    print("Monthly average: ", average)
    print()


def edit(sales):  # define edit function recieving sales as parameter
    """edits sales for a month

    Args:
        sales (list): sales
    """
    names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']  # setting names to a list of abbreviated months
    name = input("Month: ")  # get user input for month they want to edit
    name = name.title()  # making sure case sensitivity is not an issue

    for i in (names):  # loops through months in names list

        if i == name:  # checks if name from user input is in the list
            is_valid = True  # sets is valid to tru so error message is not displayed
            # setting index for placement receiving name
            index = names.index(name)
            # get user input as int for amount
            amount = int(input("Sales Amount: "))
            month = []  # set month to empty list

            month.append(name)  # append name to month list
            month.append(str(amount))  # append amount to month list
            sales[index] = month  # find correct index
            write_sales(sales)  # call write sales function

            # display that sales amount for whatever month was entered as input was modified
            print(f"Sales amount for {month[0]} was modified.")
            print()

    if not is_valid:  # if input wasn't in name list then this variable will be flagged as false
        print("Invalid three letter month")  # invalid message


def write_sales(sales):  # define write sales function receiving sales list as parameter
    """writes sales to csv file

    Args:
        sales (list): writes to csv file
    """
    with open(FILENAME, "w", newline="") as file:  # opens file with with open in write mode as file lol
        writer = csv.writer(file)  # sets writer to csv writer from modules
        writer.writerows(sales)  # write rows to sales list


if __name__ == "__main__":  # checks if main module is present
    main()  # runs main function
