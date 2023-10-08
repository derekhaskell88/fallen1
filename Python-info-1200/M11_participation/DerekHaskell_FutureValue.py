#!/usr/bin/env python3

def get_number(prompt, low, high):  # define get_number function
    """checks validation for user input

    Args:
        prompt (input): int
        low (float): main   
        high (float): main

    Returns:
        _type_: _description_
    """
    while True:  # starts infinate loop
        try:  # tries input
            number = float(input(prompt))  # get user input as float
        except ValueError:  # check for specific error
            print("Invalid Input")  # invalid message
            continue  # continues back until user enter valid input

        if number > low and number <= high:  # checks if valid input
            return number  # returns if valid
        else:  # if number is invalid
            print(f"Entry must be greater than {low} "
                  f"and less than or equal to {high}.")  # invalid int message


def get_integer(prompt, low, high):  # define get integer function
    """checks for valid input

    Args:
        prompt (input): float
        low (int): main
        high (int): main

    Returns:
        _type_: _description_
    """
    while True:  # start infinate loop
        try:  # tries input
            number = int(input(prompt))  # user input as int
        except ValueError:  # checks for specific error
            print("Invalid Input")  # invalid message
            continue  # continues back to top loop if invalid

        if number > low and number <= high:  # if valid input
            return number  # return number
        else:  # if invalid
            print(f"Entry must be greater than {low} "
                  f"and less than or equal to {high}.")  # invalid int message


# define calculate future value
def calculate_future_value(monthly_investment, yearly_interest, years):
    """calculates future value

    Args:
        monthly_investment (float): input
        yearly_interest (float): input
        years (int): input

    Returns:
        future value: interest on principal
    """
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value  # return future value


def main():  # define main function
    """main
    """
    choice = "y"  # variable for while loop
    while choice.lower() == "y":  # start while loop
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number(
            "Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print()
        # display future value
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")  # goodbye message


if __name__ == "__main__":  # if main run main
    main()  # run main
