# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 2/25/23
# Project #: MO5_P2
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import dhconverter as d  # import converter file


def fm_welcome():  # define fm_welcome function
    print("Derek Haskell's Feet and Meters Converter")  # welcome message
    print()


def fm_menu():  # define menue function
    print("Conversions Menu:\n\na. Feet to Meters\nb. Meters to Feet")


def main():  # define main function
    fm_welcome()  # run the welcome function inside of the main function
    while True:  # infinate while loop
        fm_menu()  # run the menu function inside of the main function
        # taking users input for which conversion they need
        choice = input("Select a conversion (a/b):")
        print()
        if choice == "a":  # if they choose a this will run
            feet = float(input("Enter Feet: "))  # get user input
            # use the to_meters function from the converter file
            meters = d.to_meters(feet)
            print(round(meters, 2), "Meters")  # display results

        elif choice == "b":  # if they choose b this will run
            meters = float(input("Enter Meters: "))  # get user input
            # user to_feet function from the converter file
            feet = d.to_feet(meters)
            print(round(feet, 2), "Feet")  # display results
        else:  # this will run is selection is not valid
            # display selection error
            print("You did not enter a valid selection")
        print()
        # ask user if they would like to continue
        more = input("Would you like to perform another conversion? (y/n):")
        print()
        if more != "y":  # checks to see if answer is no
            print("Thanks, Bye!")  # goodbye message is answer is no
            break


if __name__ == "__main__":  # code needed at the bottom so main function will run
    main()
