#!/usr/bin/env python3
#!/usr/bin/env python3
# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 3/18/23
# Project #: tax calculator debugging
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

tax = 0.06  # setting tax variable to six percent


def sales_tax(total):  # define sales tax function
    """
    calculates total sales tax
    """
    total = total * tax  # sales tax equeasion to find amount
    return total  # return values


def main():  # define the main function
    """
    gets user input as a float and calculates total cost after tax
    """
    print("Sales Tax Calculator\n")  # display message
    total = float(input("Enter total: "))  # get user input
    # calculate total after tax
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)  # display final total


if __name__ == "__main__":  # if the main function is there user main function this line of code is needed for main function to run
    main()
