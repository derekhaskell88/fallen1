#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import math


class triangleCalculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        solve_a(parent).grid(row=0, column=0)
        solve_b(parent).grid(row=0, column=1)
        solve_c(parent).grid(row=0, column=2)


class solve_a(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        ttk.Label(self, text="Use this equasion to solve for A\n").grid(
            row=0, column=0)
        ttk.Label(self, text="Enter Side B").grid(row=1, column=0)
        self.side_b = ttk.Entry(self)
        self.side_b.grid(row=1, column=1)
        ttk.Label(self, text="Enter Hypotenuse").grid(row=2, column=0)
        self.hypotenuse = ttk.Entry(self)
        self.hypotenuse.grid(row=2, column=1)
        ttk.Button(self, text="Calculate",
                   command=self.calculate_a).grid(row=3, column=1)
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=4, column=1)

        self.response = ttk.Label(self, text="")
        self.response.grid(row=5, column=1)

    def calculate_a(self):
        b = float(self.side_b.get())
        c = float(self.hypotenuse.get())
        a = math.sqrt(c**2-b**2)
        a = round(a, 2)
        self.response.config(text="Side A is " + str(a))

    def clear(self):
        self.side_b.delete(0, tk.END)
        self.hypotenuse.delete(0, tk.END)
        self.response.config(text="")


class solve_b(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        ttk.Label(self, text="Use this equasion to solve for B\n").grid(
            row=0, column=0)
        ttk.Label(self, text="Enter Side A").grid(row=1, column=0)
        self.side_a = ttk.Entry(self)
        self.side_a.grid(row=1, column=1)
        ttk.Label(self, text="Enter Hypotenuse").grid(row=2, column=0)
        self.hypotenuse = ttk.Entry(self)
        self.hypotenuse.grid(row=2, column=1)

        ttk.Button(self, text="Calculate",
                   command=self.calculate_b).grid(row=3, column=1)
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=4, column=1)

        self.results = ttk.Label(self, text="")
        self.results.grid(row=5, column=1)

    def calculate_b(self):
        a = float(self.side_a.get())
        c = float(self.hypotenuse.get())
        b = math.sqrt(c**2-a**2)
        b = round(b, 2)
        self.results.config(text="Side B is " + str(b))

    def clear(self):
        self.side_a.delete(0, tk.END)
        self.hypotenuse.delete(0, tk.END)
        self.results.config(text="")


class solve_c(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        ttk.Label(self, text="Use this equasion to solve for the hypotenuse\n").grid(
            row=0, column=1)
        ttk.Label(self, text="Enter Side A").grid(row=1, column=0)
        self.side_a = ttk.Entry(self)
        self.side_a.grid(row=1, column=1)
        ttk.Label(self, text="Enter Side B").grid(row=2, column=0)
        self.side_b = ttk.Entry(self)
        self.side_b.grid(row=2, column=1)
        ttk.Button(self, text="Calculate",
                   command=self.calculate_c).grid(row=3, column=1)
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=4, column=1)
        self.results = ttk.Label(self, text="")
        self.results.grid(row=5, column=1)

    def calculate_c(self):
        a = float(self.side_a.get())
        b = float(self.side_b.get())
        c = math.sqrt(a**2+b**2)
        c = round(c, 2)
        self.results.config(text="The hypotenuse is " + str(c))

    def clear(self):
        self.results.config(text="")
        self.side_a.delete(0, tk.END)
        self.side_b.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Derek Haskell's Right Triangle Calculator")
    triangleCalculator(root)
    root.mainloop()
