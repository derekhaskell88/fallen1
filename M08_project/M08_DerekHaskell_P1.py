#!/usr/bin/env python3
# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 3/25/23
# Project #: M08 project part 1 right triangle calculator
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import tkinter as tk  # import tkinter for gui
from tkinter import ttk, messagebox  # get messagebox and ttk from tkinter
import math  # import math for hypotenuse calculation


class triangle_app(ttk.Frame):  # create triangle app class the main frame root frame
    def __init__(self, parent):  # init self and parent
        ttk.Frame.__init__(self, parent)  # init frame

        # calls the triangle calculator frame
        triangleCalculator(parent).grid(row=0, column=0)
        # calls the triangle picture frame
        trianglePicture(parent).grid(row=1, column=0)


class triangleCalculator(ttk.Frame):  # create trianglecalculator class

    def __init__(self, parent):  # init self and parent
        ttk.Frame.__init__(self, parent)  # init frame
        self.parent = parent  # setting variable
        ttk.Label(self, text="Welcome to The Triangle App\n").grid(
            row=0, column=0)  # welcome message label
        ttk.Label(self, text="Enter Side A").grid(
            row=1, column=0)  # label for text
        self.side_a = ttk.Entry(self)  # for input
        self.side_a.grid(row=2, column=0)  # format on the grid
        ttk.Label(self, text="Enter Side B").grid(
            row=3, column=0)  # label for text
        self.side_b = ttk.Entry(self)  # for input
        self.side_b.grid(row=4, column=0)  # format on the grid
        ttk.Button(
            self, text="Calculate", command=self.calculate_hypotenuse).grid(row=2, column=1)  # create button for calculation
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=3, column=1)  # create button for clear
        ttk.Button(self, text="Exit", command=self.exit_app).grid(
            row=4, column=1)  # create button for exit
        self.results = ttk.Label(self, text="")  # create label for results
        self.results.grid(row=5, column=0)  # format

    def calculate_hypotenuse(self):  # define function for calculate
        a = float(self.side_a.get())  # get and float user input
        b = float(self.side_b.get())  # get and float user input
        self.message = "Number must be greater than zero"  # declare error message

        if a > 0 and b > 0:  # checks for valid input before calculating
            c = math.sqrt(a**2+b**2)
            c = round(c, 2)

        elif a <= 0 or b <= 0:  # checks for invalid input
            messagebox.showerror(
                "Error", self.message)  # calling messagebox to show error message

        # config results for calculation
        self.results.config(text="The hypotenuse is " + str(c))

    def clear(self):  # define clear function
        self.side_a.delete(0, tk.END)  # deletes entry a
        self.side_b.delete(0, tk.END)  # deletes entry b
        self.results.config(text="")  # deletes results

    def exit_app(self):  # define exit app function
        root.destroy()  # destroys root window


class trianglePicture(ttk.Frame):  # create triangle picture frame class
    def __init__(self, parent):  # initiate self and parent
        ttk.Frame.__init__(self, parent)  # initiate frame
        ttk.Label(self, text="| \\\n|   \\\n|     \\\n|       \\\n|         \\\n|           \\\n|             \\\n|_________\\").grid(
            row=0, column=0,)  # picture label


if __name__ == "__main__":  # checks to see if main is there then runs main
    root = tk.Tk()  # root window
    root.title("Derek Haskell's Right Triangle Calculator")  # root title
    root.geometry("400x300")  # root geometry
    triangle_app(root)  # triangle app is root
    root.mainloop()  # root is mainloop
