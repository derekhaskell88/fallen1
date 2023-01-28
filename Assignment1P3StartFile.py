#Name: (Derek Haskell)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 2/4/23
#Project #:1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

firstName= 'Derek' #sets Derek as variable firstName
print('Hello, my name is ' + firstName) #welcome message

school = 'Utah Valley University' #sets school variable
print('I go to ' + school) #display what school I go to using the school variable

credits = 3 #sets credits variable
classes = 6 #sets classes variable
totalcredits = (credits * classes) #equasion for totalcredits

print('If I take 6 classes this semester and all are three credits each I will be taking ') #story problem for the equasion
print(str(totalcredits) + ' credits') #display calculation

print('I would like to save money by taking this many credits.') #prints message

maxCredits = 12 #sets maxCredits variable
costPerClass = 350 #sets costPerClass variable
classFee = 20 #sets classFee variable

totalCostPerSemester = (totalcredits - maxCredits)/credits * (costPerClass + classFee) #totalCostPerSemester equasion and variable

print('If classes are free after the ' + str(maxCredits) + ' credits and each class cost $' + str(costPerClass) + ' (plus an additio') #displays the variables in a message
print('nal $' + str(classFee) + ' per class fee), I will be saving $' + str(totalCostPerSemester) + ' a semester.') #displays calculation with message

totalCostPerYear = totalCostPerSemester*3 #totalCostPerYear equasion and variable

print('That is a wopping $' + str(totalCostPerYear) + ' a year!') #displays calculation in a message

print('This was a very informative and worth while Python assignment!') #goodbye message
