#!/usr/bin/env python3

print("Welcome to Derek Haskell's Future Value Calculator")  # welcome message
print()

choice = "y"  # set variable for first while loop condition
while choice.lower() == "y":  # start first while loop
    is_valid = True  # set variable to true and boolean
    while is_valid == True:  # start second while loop
        monthly_investment = float(
            input("Enter monthly investment:\t"))  # input from user
        if monthly_investment > 0 and monthly_investment <= 1000:  # checks for valid input
            is_valid = False  # sets boolean variable to false
        else:  # if user input is invalid this will execute
            print(
                "Entry must be greater than 0 and less than or equal to 1000. Please try again.")  # error message
    is_valid = True  # setting variable back to true
    while is_valid == True:  # start third while loop
        yearly_interest_rate = float(
            input("Enter yearly interest rate:\t"))  # input from user
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:  # checks for valid input
            is_valid = False  # sets variable to false
        else:  # if user input is invalid this will execute
            print(
                "Entry must be greater than 0 and less than or equal to 15. Please try again.")  # error message
    is_valid = True  # setting variable back to true
    while is_valid == True:  # start fourth while loop
        years = int(input("Enter number of years:\t\t"))  # input from user
        if years > 0 and years <= 50:  # checks for valid input
            is_valid = False  # sets variable to false
        else:  # if user input is false this will execute
            print(
                "Entry must be greater than 0 and less than or equal to 50. Please try again.")  # error message
    monthly_interest_rate = yearly_interest_rate / \
        12 / 100  # calculate monthly interest rate
    months = years * 12  # calculate months and set it as a variable
    print()
    future_value = 0  # setting initial value equal to 0
    for i in range(1, months + 1):  # using calculation to find a range
        future_value += monthly_investment  # adding monthly investment to future value
        monthly_interest_amount = future_value * \
            monthly_interest_rate  # calculating monthly interest rate
        future_value += monthly_interest_amount  # calculating future value
        if i % 12 == 0:  # using modulo operator to check if the number is divisable by twelve
            # print a list of future values by year
            print("Year = ", i // 12, "\tFuture Value = ", round(future_value, 2))
    print()

    # asks user if they would like to continue using the application
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")  # goodbye message
