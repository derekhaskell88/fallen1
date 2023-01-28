#
#
#
#
#











print("Derek Haskell's Registration App") #app creeator
print()

firstName=input("Enter first name: ")
lastName=input("Enter last name: ")
dob=input("Enter date of birth: ")
print()

print('Welcome! ' + firstName + ' ' + lastName)
print()

print("Your registration is complete!")
tempPassword=firstName+"*"+dob
print("your temporary password is " + tempPassword)