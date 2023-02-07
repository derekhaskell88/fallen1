# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 2/18/23
# Project #: MO4_P1
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

print("Derek Haskell's Letter Grade Converter")  # welcome message
print()

choice = "y"  # variable for while loop
while choice.lower() == "y":  # starting while loop
    # taking input from user as an integer
    number = int(input("Enter numerical grade: "))
    if number <= 100 and number >= 94:  # create an if statement that will determine the users grade based off of their input
        print("Letter grade: A")
    elif number <= 93 and number >= 90:
        print("Letter grade: A-")
    elif number <= 89 and number >= 87:
        print("Letter grade: B+")
    elif number <= 86 and number >= 83:
        print("Letter grade: B")
    elif number <= 82 and number >= 80:
        print("Letter grade: B-")
    elif number <= 79 and number >= 77:
        print("Letter grade: C+")
    elif number <= 76 and number >= 73:
        print("Letter grade: C")
    elif number <= 72 and number >= 70:
        print("Letter grade: C-")
    elif number <= 69 and number >= 67:
        print("Letter grade: D+")
    elif number <= 66 and number >= 63:
        print("Letter grade: D")
    elif number <= 62 and number >= 60:
        print("Letter grade: D-")
    else:
        print("Letter grade: E")
    print()
    # taking user input to see if they want to continue
    choice = input("Continue (y/n)?: ")
    print()
print("Bye!")  # goodbye message
