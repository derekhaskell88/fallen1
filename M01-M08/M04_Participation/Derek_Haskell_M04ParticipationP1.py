#!/usr/bin/env python3

# display a welcome message
print("Derek Haskell's Miles Per Gallon application")
print()

another_trip = "y"  # set variable for while loop
while another_trip.lower() == "y":  # starts while loop
    # get input from the user for miles driven gallons used and cost per gallon
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter Cost per gallon:      "))
    total_gas_cost = round(gallons_used * cost_per_gallon,
                           1)  # calculate total gas cost
    cost_per_mile = round(total_gas_cost / miles_driven,
                          1)  # calculate cost per mile
    mpg = round((miles_driven / gallons_used), 2)  # calculate miles per gallon
    if miles_driven <= 0:  # starting if statement that makes sure the input from the user is valid
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:  # if input is valid then calculations will be displayed

        print()
        # display and format calculations
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost)
        print("Cost Per Mile:             ", cost_per_mile)
        print()
        # seeing if user wants to continue
        another_trip = input('Get entries for another trip (y/n)? ')
        print()

print("Bye")  # goodbye message
