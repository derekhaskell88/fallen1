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
print('Tax Amount: $' + "{:.2f}".format(taxAmount))  # display tax amount
takeHomePay = grossPay-taxAmount  # equasion
# display take home pay
print('Take Home Pay: $' + "{:.2f}".format(takeHomePay))
