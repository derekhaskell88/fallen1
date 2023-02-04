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

print("Derek Haskell's Tip Calculator App")  # app creator
print()

costOfMeal = float(input('Cost of meal: $'))  # taking usser input
tipPercent = float(input('Tip percent: '))  # taking user input
print()

tipAmount = costOfMeal*(tipPercent/100)  # equasion
print('Tip amount: $' + "{:.2f}".format(tipAmount))  # display tip amount
totalAmount = costOfMeal+tipAmount  # equasion
print('Total amount: $' + "{:.2f}".format(totalAmount))  # display total amount
