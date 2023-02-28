#!/usr/bin/env python3
# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 3/18/23
# Project #: guessing game debugging
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import random  # importing the random module


def display_title():  # defining display title function
    """
    displays the title
    """
    # printing the display asking user to guess number
    print("Guess the number!")
    print()


def get_limit():  # defining the get limit function
    """
    get user input for range of numbers

    Returns:
      _type_: integer _description_ upper limit
    """
    # get user input for the range
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit  # return the value for limit


def play_game(limit):  # define the play game function
    """
    takes user input as guesses 
    the game
    """
    # generate a random number between 1 and users input for limit
    number = random.randint(1, limit)
    count = 0  # setting the count variable
    # start the game display the range for the guesses
    print(f"I'm thinking of a number from 1 to {limit}\n")

    while True:  # start infinate while loop
        # get user input and store as integer
        guess = int(input("Your guess: "))
        if guess < number:  # start if statement that will run if guess is less than number
            print("Too low.")  # displays if guess is too low
            count += 1  # adds 1 to guess count
        elif guess > number:  # runs if guess is greater than number
            print("Too high.")  # too high message
            count += 1  # adds 1 to guess count
        elif guess == number:  # runs if guess equals number
            count += 1  # adds 1 to guess count
            print(f"You guessed it in {count} tries.\n")  # correct message
            return  # return values


def main():  # define main function
    """
    main function calls display title, get limit, and play game functions
    """
    display_title()  # run display title function with 0 pararmeters

    again = "y"  # setting variable for while loop
    while again.lower() == "y":  # start while loop

        # calling the get limit function to get limit and set it equal to limit variable
        limit = get_limit()
        play_game(limit)  # call the play game function with the limit variable

        # ask user if they want to play again
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")  # goodbye message


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
