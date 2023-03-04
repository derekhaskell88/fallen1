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


class mathExam:  # main class only class
    def __init__(self, parent):  # initiate self and parent

        self.question_label = ttk.Label(
            parent, text="What is the cube root of 64?")  # create label and display text
        self.question_label.pack()  # pack and format

        self.answer_entry = ttk.Entry(parent)  # create entry box for input
        self.answer_entry.pack()  # format

        self.submit_button = ttk.Button(
            parent, text="Submit", command=self.grade_question)  # create button
        self.submit_button.pack()  # format

        self.response_label = ttk.Label(
            parent, text="")  # create label for score
        self.response_label.pack()  # format

    def grade_question(self):  # grades question
        answer = self.answer_entry.get()  # get variable
        if answer == "4":  # check value
            response = "Correct!"  # correct answer
        else:  # runs if incorrect
            response = "Incorrect. The correct answer is 4."  # wrong answer
        self.response_label.configure(text=response)  # configure text


if __name__ == '__main__':  # if the main is there call main loop
    root = tk.Tk()  # setting root equal to tk for gui
    root.title("Math Exam")  # set title of window
    root.geometry("500x500")  # size of window
    mathExam(root)  # setting root frame to the math exam class
    frame = ttk.Frame(root, padding="10 10 10 10")  # set the frame parameters
    frame.pack(fill=tk.BOTH, expand=True)  # format the frame

    root.mainloop()  # root is the main loop set root to main
