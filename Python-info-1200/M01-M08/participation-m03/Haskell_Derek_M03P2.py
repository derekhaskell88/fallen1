#!/usr/bin/env python3
print("Derek Haskell's Test Scores App")  # welcome message
print()
print("Enter 3 test scores")  # instructions
print("======================")  # aesthetic

# get scores from the user
score1 = int(input("Enter test score: "))
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))
total_score = score1 + score2 + score3  # calculate total scores
average_score = round(total_score / 3)  # calculate average score

# format and display the result
print("======================")  # aesthetic
# print('Your Scores: ' + str(score1) + ' ' + str(score2) + ' ' + str(score3))
# print all three scores then total score then average score
print('Your Scores:  ', score1, score2, score3)
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye")  # goodbye message
