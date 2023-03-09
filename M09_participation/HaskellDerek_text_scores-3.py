#!/usr/bin/env python3

def display_welcome():  # welcome message function
    """
    displays welcome message
    """
    print("The Test Scores program")  # welcome message
    print("Enter 'x' to exit")  # instruction
    print("")


def get_scores():  # get scores function
    """
    gets user input get scores

    Returns:
      scores after user types x  _type_: _description_
    """
    scores = []  # scores is a list
    while True:  # start while loop
        score = input("Enter test score: ")  # get user input
        if score == "x":  # check is x to see if user is done inputting scores
            return scores
        else:
            score = int(score)  # convert score to int
            if score >= 0 and score <= 100:  # makes sure input is valid
                scores.append(score)  # append user input to the scores list
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")  # invalid message


def process_scores(scores):
    """
    processes scores

    Args:
      takes user input and calculates average mean and median  scores (_type_): _description_
    """
    # calculate average score
    scores.sort()
    median = 0  # declaring variables
    total = 0
    for score in scores:  # start for loop using scores list as range
        total += score  # declaring variable
    num_scores = len(scores)  # declaring variable
    average = total / num_scores  # calc average
    low_score = min(scores)  # calc low score
    high_score = max(scores)  # calc high score
    median_index = num_scores // 2  # calc median index
    if num_scores % 2 == 1:  # calc median
        median = scores[median_index]  # calc median if odd
    else:
        middle_1 = scores[median_index]
        middle_2 = scores[median_index - 1]
        median = (middle_1 + middle_2) / 2  # calc median if even

    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", num_scores)
    print("Average Score:     ", average)
    print("Low Score:     ", low_score)
    print("High Score:     ", high_score)
    print("Median Score:     ", median)


def main():
    """
    main function 
    """
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")


# if started as the main module, call the main function
if __name__ == "__main__":  # run main as main
    main()
