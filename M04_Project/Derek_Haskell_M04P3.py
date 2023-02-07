# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 2/18/23
# Project #: MO4_P3
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

print("Derek Haskell's Change App")  # welcome message
print()

choice = "y"  # variable for while loop
while choice.lower() == "y":  # starting while loop
    cents = int(input("Enter number of cents (0-99): "))  # taking user input
    print()
    # calculates how many quarters will divide into the users input equally
    quarters = cents // 25
    print("Quarters:", quarters)  # displays calculation
    cents = cents % 25  # calculates the remainder after quarters are established
    # calculates how many dimes will divide into the remaining number equally
    dimes = cents // 10
    print("Dimes:\t ", dimes)  # displays calculation
    cents = cents % 10  # calculates the remainder after dimes are established
    # calculates how many nickles will divide into the remaining number equally
    nickles = cents // 5
    print("Nickles: ", nickles)  # displays calculation
    cents = cents % 5  # calculates the remainder after knickles are established
    pennies = cents // 1  # calculates how many pennies divide into the remainder equally
    print("Pennies: ", pennies)  # display calculation
    print()
    # ask user if they want to continue then take input
    choice = input("Continue? (y/n) ")
    print()
print("Bye!")  # goodbye message
