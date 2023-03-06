#!/usr/bin/env python3
# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 3/25/23
# Project #: M08 project part 2 right triangle and cylinder calculator
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import tkinter as tk  # import tkinter for gui
from tkinter import ttk, messagebox  # get ttk and messagebox as well
import math  # importing math needed for the triangle calculator


# creating main class that runs all four frames
class geometry_calculator(ttk.Frame):
    def __init__(self, parent):  # define init self and parent
        ttk.Frame.__init__(self, parent)  # initiate frame

        # call the triangle calculator frame
        triangle_calculator(parent).grid(row=0, column=0)
        # call the cylinder calculator frame
        cylinder_calculator(parent).grid(row=0, column=1)
        # call the triangle picture frame
        trianglePicture(parent).grid(row=1, column=0)
        # call the cylinder picture frame
        cylinderPicture(parent).grid(row=1, column=1)

        ttk.Button(parent, text="Exit", command=self.exit_app).grid(
            row=2, column=1)  # create button for exiting application

    def exit_app(self):  # define command for exit button
        """
        exits app
        """
        root.destroy()  # destroys root window


class triangle_calculator(ttk.Frame):  # the triangle calculator class
    def __init__(self, parent):  # define init self and parent
        # initiate frame
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        ttk.Label(self, text="Triangle App\n").grid(
            row=0, column=0)  # App title
        ttk.Label(self, text="Enter Side A").grid(
            row=1, column=0)  # create a label for text
        self.side_a = ttk.Entry(self)  # create a label for entry
        self.side_a.grid(row=2, column=0)  # format grid
        ttk.Label(self, text="Enter Side B").grid(
            row=3, column=0)  # create a label for text
        self.side_b = ttk.Entry(self)  # create a label for entry
        self.side_b.grid(row=4, column=0)  # format grid
        ttk.Button(
            self, text="Calculate", command=self.calculate_hypotenuse).grid(row=2, column=1)  # create a button to calculate
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=3, column=1)  # create a button to clear text
        self.results = ttk.Label(self, text="")  # create a label for text
        self.results.grid(row=5, column=0)  # format grid

    def calculate_hypotenuse(self):  # define the function to calculate hypotenuse
        """
        calculates hypotenuse of a right triangle
        """
        a = float(self.side_a.get())  # get user input and float it
        b = float(self.side_b.get())  # get user input and float it
        self.message = "Number must be greater than zero"  # setting error message

        if a > 0 and b > 0:  # make sure both entries are greater than zero
            c = math.sqrt(a**2+b**2)  # calculate hypotenuse
            c = round(c, 2)  # round calculation

        elif a <= 0 or b <= 0:  # checks for invalid input
            messagebox.showerror(
                "Error", self.message)  # calling messagebox to showerror

        # configure text for results after calculation
        self.results.config(text="The hypotenuse is " + str(c))

    def clear(self):  # making clear command to clear text
        """
        clears user input and results from calculations
        """
        self.side_a.delete(0, tk.END)  # clear a
        self.side_b.delete(0, tk.END)  # clear b
        self.results.config(text="")  # clear results


class cylinder_calculator(ttk.Frame):  # cylincer calculator frame
    def __init__(self, parent):  # define init self and parent
        # initiate frame
        # create frame init frame
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        ttk.Label(self, text="Cylinder App\n").grid(
            row=0, column=0)  # App title
        ttk.Label(self, text="Enter Diameter").grid(
            row=1, column=0)  # create a label for text
        self.diameter = ttk.Entry(self)  # create a label for entry
        self.diameter.grid(row=2, column=0)  # format grid
        ttk.Label(self, text="Enter Heighth").grid(
            row=3, column=0)  # create a label for text
        self.heighth = ttk.Entry(self)  # create a label for entry
        self.heighth.grid(row=4, column=0)  # format grid

        ttk.Button(self, text="Calculate",
                   command=self.calculate).grid(row=2, column=1)  # create button to calculate
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=3, column=1)  # create button to clear text
        self.circumference = ttk.Label(
            self, text="")  # create label for results
        self.circumference.grid(row=5, column=0)  # format grid

        self.volume = ttk.Label(self, text="")  # create a label for text
        self.volume.grid(row=6, column=0)  # format grid

    def calculate(self):  # define calculate function
        """
        calculates circumference and volume if user inputs heighth and diameter
        """
        diameter = float(self.diameter.get())  # get user input
        heighth = float(self.heighth.get())  # get user input
        self.message = "Number must be greater than 0"  # set message for invalid entry
        if diameter > 0 and heighth > 0:  # checks to see if entries are valid
            radius = round(diameter/2, 2)  # calculate radius
            # calculate circumference
            circumference = round(3.14 * radius**2, 2)
            # calculate and round volume
            volume = round(3.14 * radius**2 * heighth, 2)

        else:  # runs if input is invalid
            messagebox.showerror("Error", self.message)  # pop up message box
        # configure text for circumference label
        self.circumference.config(text="Circumference = " + str(circumference))
        # configure text for results for volume
        self.volume.config(text="Volume = " + str(volume))

    def clear(self):  # define clear button function
        """
        clears user input and results from calculations
        """
        self.circumference.config(text="")  # clears results
        self.volume.config(text="")  # clears volume results
        self.diameter.delete(0, tk.END)  # clears text
        self.heighth.delete(0, tk.END)  # clears text


class trianglePicture(ttk.Frame):  # create triangle picture frame class
    def __init__(self, parent):  # define init self and parent
        ttk.Frame.__init__(self, parent)  # initiate frame
        ttk.Label(self, text="| \\\n|   \\\n|     \\\n|       \\\n|         \\\n|           \\\n|             \\\n|_________\\").grid(
            row=0, column=0,)  # create label for triangle picture


class cylinderPicture(ttk.Frame):  # create cylinder picture frame
    def __init__(self, parent):  # define init self and parent
        ttk.Frame.__init__(self, parent)  # initiate frame self parent
        ttk.Label(self, text="____________\n(                   )\n|                  |\n|                  |\n|                  |\n|                  |\n(___________)\n").grid(
            row=0, column=0,)  # create label for cylinder picture


if __name__ == "__main__":  # checks if main then runs main
    root = tk.Tk()  # setting root equal to tk for frame
    root.title("Derek Haskell's Geometry Calculator")  # setting root title
    geometry_calculator(root)  # setting geometry calculator as the root frame
    root.mainloop()  # setting root as main loop
