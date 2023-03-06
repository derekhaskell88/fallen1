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
# version 1.0

import tkinter as tk
from tkinter import ttk
import math


class triangleCalculator:
    def __init__(self, parent):
        ttk.Label(
            parent, text="Welcome to Derek Haskell's Right Triangle Calculator").pack()
        ttk.Label(parent, text="You must enter a 0 for the missing side").pack()
        ttk.Label(parent, text="Enter Side A").pack()

        self.side_A = ttk.Entry(parent)
        self.side_A.pack()

        ttk.Label(parent, text="Enter Side B").pack()

        self.side_B = ttk.Entry(parent)
        self.side_B.pack()

        ttk.Label(parent, text="Enter Side C").pack()

        self.side_C = ttk.Entry(parent)
        self.side_C.pack()

        ttk.Button(parent, text="Calculate", command=self.calculate).pack()
        ttk.Button(parent, text="Clear", command=self.clear_text).pack()
        ttk.Button(parent, text="Close", command=self.close_app).pack()

        self.output = ttk.Label(parent, text="")
        self.output.pack()

        self.error = ttk.Label(parent, text="")
        self.error.pack()

    def calculate(self):
        a = float(self.side_A.get())
        b = float(self.side_B.get())
        c = float(self.side_C.get())

        if a == 0:
            answer = math.sqrt(c**2 - b**2)
            response = "Side A"
        elif b == 0:
            answer = math.sqrt(c**2 - a**2)
            response = "Side B"
        elif c == 0:
            answer = math.sqrt(a**2 + b**2)
            response = "Side C"
        else:
            self.error.config(text="You must enter a 0 for the missing side.")
        answer = round(answer, 2)
        self.output.config(text=str(response) +
                           " = " + str(answer))

    def clear_text(self):
        self.side_A.delete(0, tk.END)
        self.side_B.delete(0, tk.END)
        self.side_C.delete(0, tk.END)
        self.output.config(text="")
        self.error.config(text="")

    def close_app(self):
        root.destroy()


root = tk.Tk()
root.title("Right Triangle Calculator")
root.geometry("500x700")
triangleCalculator(root)
root.mainloop()  # setting root as the main loop
