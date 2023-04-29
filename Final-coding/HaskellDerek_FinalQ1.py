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

tax = 0.06  # settig tax variable equal to six percent


def sales_tax(t):  # defining the sales tax function
    """takes floated user input then calculates and returns sales tax
    """
    sales_tax = t * tax  # calculates sales tax
    return sales_tax  # returns sales tax


def main():  # defining the main function
    """main function displays welcome message then asks for user input. It then displays total after tax"""
    print("Sales Tax Calculator\n")  # print welcome message
    total = float(input("Enter total: "))  # floating user input
    # calculates total after tax
    total_after_tax = round(total + sales_tax(total), 2)
    # displays users total after tax
    print("Total after tax: ", total_after_tax)


if __name__ == "__main__":  # if there is a main module then run main as the main module
    main()  # calling main function
