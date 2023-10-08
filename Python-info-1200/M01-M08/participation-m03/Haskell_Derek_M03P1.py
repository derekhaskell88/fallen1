#!/usr/bin/env python3
print("Derek Haskell's MPG App")  # welcome message
print()

# get float input from the user for miles driven, gallons used, and cost per gallon
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))
print()

# calculate miles per gallon, total gas cost, and cost of gas per mile
# round calculated results
mpg = round(miles_driven / gallons_used, 1)
total_gas_cost = round(cost_per_gallon * gallons_used, 2)
cost_per_mile = round(total_gas_cost / miles_driven, 2)

# format and display the results as a string
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas cost:\t\t\t" + str(total_gas_cost))
print("Cost Per mile:\t\t\t" + str(cost_per_mile))
print("Bye")  # goodbye message
