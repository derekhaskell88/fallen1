#!/usr/bin/env python3
# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 2/11/2023
# Project #:2
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

print("Welcome to the app bundle!")
play = "y"
while play == "y":
    print("Enter 1 for Student Registration")
    print("Enter 2 for Pay Check Calculator")
    print("Enter 3 for Tip Calculator")
    app = int(input('-----> '))
    if app == 1:
        print("Derek Haskell's Registration App")  # app creeator
        print()

        # gather information from user
        firstName = input("Enter first name: ")  # get first name as input
        lastName = input("Enter last name: ")  # get last name as input
        dob = input("Enter date of birth: ")  # get dob as input
        print()

        print('Welcome ' + firstName + ' ' + lastName + '!')  # welcome user
        print()

        # registration completed sucessful message
        print("Your registration is complete!")
        tempPassword = firstName+"*"+dob  # calculate temporary password
        # show user their temporary password
        print("your temporary password is " + tempPassword)
    elif app == 2:
        print("Derek Haskell's Pay Check Calculator App")  # writer intro
        print()

        hoursWorked = float(input('Hours worked: '))  # taking input from user
        payRate = float(input('Hourly pay rate: '))  # taking input from user
        print()

        grossPay = hoursWorked*payRate  # equasion
        print('Gross pay: $' + "{:.2f}".format(grossPay))  # display gross pay
        taxRate = 18  # set taxrate variable
        print("Tax Rate: " + str(taxRate) + '%')  # display tax rate
        taxAmount = grossPay*(taxRate/100)  # equasion
        # display tax amount
        print('Tax Amount: $' + "{:.2f}".format(taxAmount))
        takeHomePay = grossPay-taxAmount  # equasion
        # display take home pay
        print('Take Home Pay: $' + "{:.2f}".format(takeHomePay))
    else:
        print("Derek Haskell's Tip Calculator App")  # app creator
        print()

        costOfMeal = float(input('Cost of meal: $'))  # taking usser input
        tipPercent = float(input('Tip percent: '))  # taking user input
        print()

        tipAmount = costOfMeal*(tipPercent/100)  # equasion
        # display tip amount
        print('Tip amount: $' + "{:.2f}".format(tipAmount))
        totalAmount = costOfMeal+tipAmount  # equasion
        # display total amount
        print('Total amount: $' + "{:.2f}".format(totalAmount))
    print()
    print("Thank you for using the app bundle!")
    play = input("Would you like to use another app (y/n) ")
    print()
    print("---------------------------------------------")
    print()
