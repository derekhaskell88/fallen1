# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 2/18/23
# Project #: MO4_P2
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

print("Derek Haskell's Tip Calculator")  # welcome message
print()

cost_of_meal = float(input("Enter cost of meal: "))  # taking user input
print()

for i in range(15, 30, 5):  # setting up for loop
    tip_amount = round(i / 100 * cost_of_meal, 2)  # calculate tip amount
    # calculate total cost of meal
    total_cost_of_meal = round(cost_of_meal + tip_amount, 2)
    print(str(i) + '%\nTip amount:  ', tip_amount,
          '\nTotal amount:', total_cost_of_meal)  # print results for range defined earlier with each different calculated result
    print()
