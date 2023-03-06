#!/usr/bin/env python3
# Name: (Derek Haskell)
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 3/25/23
# Project #: M08 project right triangle calculator
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

import tkinter as tk
from tkinter import ttk, messagebox
import math


class geometry_calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        triangle_calculator(parent).grid(row=0, column=0)
        cylinder_calculator(parent).grid(row=0, column=1)
        trianglePicture(parent).grid(row=1, column=0)
        cylinderPicture(parent).grid(row=1, column=1)

        ttk.Button(parent, text="Exit", command=self.exit_app).grid(
            row=2, column=1)

    def exit_app(self):
        root.destroy()


class triangle_calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        ttk.Label(self, text="Triangle App\n").grid(
            row=0, column=0)
        ttk.Label(self, text="Enter Side A").grid(row=1, column=0)
        self.side_a = ttk.Entry(self)
        self.side_a.grid(row=2, column=0)
        ttk.Label(self, text="Enter Side B").grid(row=3, column=0)
        self.side_b = ttk.Entry(self)
        self.side_b.grid(row=4, column=0)
        ttk.Button(
            self, text="Calculate", command=self.calculate_hypotenuse).grid(row=2, column=1)
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=3, column=1)
        self.results = ttk.Label(self, text="")
        self.results.grid(row=5, column=0)

    def calculate_hypotenuse(self):
        a = float(self.side_a.get())
        b = float(self.side_b.get())
        self.message = "Number must be greater than zero"

        if a > 0 and b > 0:
            a = float(self.side_a.get())
            b = float(self.side_b.get())
            c = math.sqrt(a**2+b**2)
            c = round(c, 2)

        elif a <= 0 or b <= 0:
            messagebox.showerror(
                "Error", self.message)

        self.results.config(text="The hypotenuse is " + str(c))

    def clear(self):
        self.side_a.delete(0, tk.END)
        self.side_b.delete(0, tk.END)
        self.results.config(text="")


class cylinder_calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        ttk.Label(self, text="Cylinder App\n").grid(
            row=0, column=0)
        ttk.Label(self, text="Enter Diameter").grid(row=1, column=0)
        self.diameter = ttk.Entry(self)
        self.diameter.grid(row=2, column=0)
        ttk.Label(self, text="Enter Heighth").grid(row=3, column=0)
        self.heighth = ttk.Entry(self)
        self.heighth.grid(row=4, column=0)

        ttk.Button(self, text="Calculate",
                   command=self.calculate).grid(row=2, column=1)
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=3, column=1)
        self.circumference = ttk.Label(self, text="")
        self.circumference.grid(row=5, column=0)

        self.volume = ttk.Label(self, text="")
        self.volume.grid(row=6, column=0)

    def calculate(self):
        diameter = float(self.diameter.get())
        heighth = float(self.heighth.get())
        self.message = "Number must be greater than 0"
        if diameter > 0 and heighth > 0:
            radius = round(diameter/2, 2)
            circumference = round(3.14 * radius**2, 2)
            volume = round(3.14 * radius**2 * heighth, 2)

        else:
            messagebox.showerror("Error", self.message)
        self.circumference.config(text="Circumference = " + str(circumference))
        self.volume.config(text="Volume = " + str(volume))

    def clear(self):
        self.circumference.config(text="")
        self.volume.config(text="")
        self.diameter.delete(0, tk.END)
        self.heighth.delete(0, tk.END)


class trianglePicture(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text="| \\\n|   \\\n|     \\\n|       \\\n|         \\\n|           \\\n|             \\\n|_________\\").grid(
            row=0, column=0,)


class cylinderPicture(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text="____________\n(                   )\n|                  |\n|                  |\n|                  |\n|                  |\n(___________)\n").grid(
            row=0, column=0,)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Derek Haskell's Geometry Calculator")
    # root.geometry("600x600")
    geometry_calculator(root)
    root.mainloop()
