#!/usr/bin/env python3
# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 3/23/23
# Project #: basic gui math test
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.


import tkinter as tk  # import the tkinter module as tk
from tkinter import ttk  # get ttk from tkinter


class MathExam:  # main class only class
    def __init__(self, parent):  # initiate self and parent

        self.question_Label = ttk.Label(
            parent, text="What is the cube root of 64?")  # create label and display text
        self.question_Label.pack()  # pack and format

        self.answer_entry = ttk.Entry(parent)  # create entry box for input
        self.answer_entry.pack()  # format

        self.submit_button = ttk.Button(
            parent, text="Submit", command=self.grade_question)  # create button
        self.submit_button.pack()  # format

        self.response_Label = ttk.Label(
            parent, text="")  # create label for score
        self.response_Label.pack()  # format

        self.question2_Label = ttk.Label(
            parent, text="What is the greatest common factor of 64x, 16xy, 4xyz")  # label for question 2
        self.question2_Label.pack()  # format label

        self.answer_entry2 = ttk.Entry(parent)  # create entry box for input
        self.answer_entry2.pack()  # format

        self.submit_button2 = ttk.Button(
            parent, text="Submit", command=self.grade_question_two)  # create button 2
        self.submit_button2.pack()  # format button

        self.response_Label2 = ttk.Label(
            parent, text="")  # make label for score
        self.response_Label2.pack()  # format

        self.question3_Label = ttk.Label(
            parent, text="what is the value of i squared?")  # make label for question 3
        self.question3_Label.pack()  # format

        self.answer_entry3 = ttk.Entry(parent)  # get user input
        self.answer_entry3.pack()  # format entry box

        self.submit_button3 = ttk.Button(
            parent, text="Submit", command=self.grade_question_three)  # make button 3
        self.submit_button3.pack()  # format

        self.response_Label3 = ttk.Label(
            parent, text="")  # make label for score
        self.response_Label3.pack()  # format

    def grade_question(self):  # grades number 1
        answer = self.answer_entry.get()  # get variable
        if answer == "4":  # check value
            response = "Correct!"  # correct answer
        else:  # runs if incorrect
            response = "Incorrect. The correct answer is 4."  # wrong answer
        self.response_Label.configure(text=response)  # configure text

    def grade_question_two(self):  # grades number 2
        answer_two = self.answer_entry2.get()  # retrieving user input for question 2
        if answer_two == "4x":  # check if correct
            response = "Correct!"  # if corect sset response
        else:  # if incorrect
            response = "Incorrect. The correct answer is 4x."  # set incorrect response
        # configure text as response
        self.response_Label2.configure(text=response)

    def grade_question_three(self):  # grades number 3
        answer_three = self.answer_entry3.get()  # retrieve user input from question 3
        if answer_three == "-1":  # checks if correct answer
            response = "Correct!"  # set response
        else:  # if incorrect
            response = "Incorrect. The correct answer is -1."  # set response variable
        self.response_Label3.configure(
            text=response)  # configure text response


if __name__ == '__main__':  # if the main is there call main loop
    root = tk.Tk()  # setting root equal to tk for gui
    root.title("Math Exam")  # set title of window
    root.geometry("500x500")  # size of window
    MathExam(root)  # setting root frame to the math exam class
    frame = ttk.Frame(root, padding="10 10 10 10")  # set the frame parameters
    frame.pack(fill=tk.BOTH, expand=True)  # format the frame

    root.mainloop()  # root is the main loop set root to main
