#Name: (Derek Haskell)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 
#Project #:2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Derek Haskell's Pay Check Calculator App")

hoursWorked=float(input('Hours worked: '))
payRate=float(input('Hourly pay rate: '))
print()

grossPay=hoursWorked*payRate
print('Gross pay: $' + "{:.2f}".format(grossPay))
taxRate=0.18
print("Tax Rate: " + str(taxRate))