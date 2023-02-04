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
