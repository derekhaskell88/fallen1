# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 2/25/23
# Project #: MO5_P1
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

print("Derek Haskell's Even or Odd Checker")  # welcome message
print()


def is_even(num):  # define is even function
    """
    determines if number is even or odd
    """
    if num % 2 == 0:  # using modulo to determine if number is even
        return True  # if even returns true
    else:  # elsse statement that will return false if odd
        return False  # returns false if odd


def main():  # define main function
    """
    main function gets user input and calls is_even function
    """
    choice = "y"  # variable for while loop
    while choice.lower() == "y":  # start while loop
        print("Derek's even or odd checker")  # welcome message
        print()
        # get input from user as an ninteger
        my_num = int(input("Enter an integer: "))
        # runs users input through the is even function to determine if True
        if is_even(my_num) == True:
            print("This is an even number")  # if true it is even
        else:  # runs if false
            print("This is an odd number")  # prints if false
        print()
        # see if user would like to continue
        choice = input("Continue (y/n)? ")
        print()
    print("Bye!")  # goodbye message


if __name__ == "__main__":  # code needed at the end for main function to run
    main()
