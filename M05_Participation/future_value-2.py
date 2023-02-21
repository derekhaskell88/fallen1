#!/usr/bin/env python3

import validate as v  # imporing the validation file

print("Derek Haskell's Validated Future Value App")  # welcome message
print()


# define and calculate future value function
def calculate_future_value(monthly_investment, yearly_interest, years):
    """
    calculates future value based on user input
    """
    monthly_interest_rate = yearly_interest / 12 / \
        100  # equasion for monthly interest rate
    months = int(years * 12)  # finding number of months

    # equasion to calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value  # returning the value for future value variable


def main():  # define the main function
    """
    main function used to get user input for monthly investment as a float and yearly interest as an integer uses validate file
    """
    choice = "y"  # setting up while loop variable
    while choice.lower() == "y":  # starting while loop
        # get input from the user and invorperating the validate file with v.get_float and v.get_int
        monthly_investment = v.get_float(
            "Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = v.get_float(
            "Enter yearly interest rate:\t", 0, 15)
        years = v.get_int("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        print()
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")  # goodbye message


if __name__ == "__main__":  # code needed at the end so that the main function will execute
    main()
