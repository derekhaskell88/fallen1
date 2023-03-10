#!/usr/bin/env python3
print("Derek Haskell's Rectangle App")  # welcome message
print()

# get input from the user then float the input for length and width
length = float(input("Please enter the length: "))
width = float(input("Please enter the width:  "))

# calculate area and perimeter of a rectangle
area = round(length * width, 2)  # equasion
perimeter = round(length * 2 + width * 2, 2)  # equasion

# format and display the results
print()
print("Area:\t\t" + str(area))  # display area
print("Perimeter:\t" + str(perimeter))  # display perimeter
print()
print("Thanks for using this program!")  # thank you message
