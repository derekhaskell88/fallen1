import tkinter as tk
from tkinter import ttk, messagebox
import math


class function_calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        # self.pack(fill=tk.BOTH, expand=True)

        trinomial_calculator(parent).grid(row=0, column=0)
        third_degree_calculator(parent).grid(row=0, column=1)
        ttk.Button(parent, text="Exit", command=self.exit_app).grid(
            row=1, column=1, sticky=tk.E, padx=5, pady=5)

    def exit_app(self):
        root.destroy()


class trinomial_calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        ttk.Label(self, text="Trinomial Calculator").grid(
            row=0, column=1, sticky=tk.E)
        ttk.Label(self, text="Enter leading coefficient").grid(
            row=1, column=0, sticky=tk.E)
        ttk.Label(self, text="Enter second coefficient").grid(
            row=2, column=0, sticky=tk.E)
        ttk.Label(self, text="Enter constant term").grid(
            row=3, column=0, sticky=tk.E)
        ttk.Label(self, text="Enter x value").grid(
            row=4, column=0, sticky=tk.E)
        ttk.Button(self, text="Calc Int", command=self.calculate_intercepts).grid(
            row=2, column=3)
        ttk.Button(self, text="Calc Vert", command=self.calculate_vertex).grid(
            row=3, column=3)
        ttk.Button(self, text="Calc Y",
                   command=self.calculate_y).grid(row=4, column=3)
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=5, column=3)

        self.leading_coefficient = ttk.Entry(self)
        self.leading_coefficient.grid(row=1, column=1)
        self.second_coefficient = ttk.Entry(self)
        self.second_coefficient.grid(row=2, column=1)
        self.constant_term = ttk.Entry(self)
        self.constant_term.grid(row=3, column=1)
        self.x_value = ttk.Entry(self)
        self.x_value.grid(row=4, column=1)
        self.results = ttk.Label(self, text="")
        self.results.grid(row=5, column=1)

    def calculate_y(self):
        a = float(self.leading_coefficient.get())
        b = float(self.second_coefficient.get())
        c = float(self.constant_term.get())
        x = float(self.x_value.get())
        y = round((a*(x**2))+(b*x)+c, 2)
        self.results.config(text="Y = " + str(y))

    def calculate_intercepts(self):
        a = float(self.leading_coefficient.get())
        b = float(self.second_coefficient.get())
        c = float(self.constant_term.get())
        step1 = math.sqrt(b**2 + -4*a*c)
        step2 = (-1*b+step1)/(2*a)
        step3 = (-1*b-step1)/(2*a)
        x_int1 = round(step3, 2)
        x_int2 = round(step2, 2)
        y_int = round((a*(0**2))+(b*0)+c, 2)
        self.results.config(text="X Int: " +
                            str(x_int1) + ", " + str(x_int2) + "\nY Int: " + str(y_int))

    def calculate_vertex(self):
        a = float(self.leading_coefficient.get())
        b = float(self.second_coefficient.get())
        c = float(self.constant_term.get())
        x = round((-1*b)/(2*a), 2)
        y = round((a * (x**2)) + (b*x) + c, 2)
        self.results.config(text="X = " + str(x) + ", Y = " + str(y))

    def clear(self):
        self.leading_coefficient.delete(0, tk.END)
        self.second_coefficient.delete(0, tk.END)
        self.constant_term.delete(0, tk.END)
        self.x_value.delete(0, tk.END)
        self.results.config(text="")


class third_degree_calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        ttk.Label(self, text="Third Degree Calculator").grid(
            row=0, column=1, sticky=tk.E)
        ttk.Label(self, text="Enter leading coefficient").grid(
            row=1, column=0, sticky=tk.E)
        ttk.Label(self, text="Enter second coefficient").grid(
            row=2, column=0, sticky=tk.E)
        ttk.Label(self, text="Enter third coefficient").grid(
            row=3, column=0, sticky=tk.E)
        ttk.Label(self, text="Enter constant term").grid(
            row=4, column=0, sticky=tk.E)
        ttk.Label(self, text="Enter x value").grid(
            row=5, column=0, sticky=tk.E)
        ttk.Button(self, text="Calc Int", command=self.calculate_intercepts).grid(
            row=3, column=3)
        ttk.Button(self, text="Calc Y",
                   command=self.calculate_y).grid(row=4, column=3)
        ttk.Button(self, text="Clear", command=self.clear).grid(
            row=5, column=3)

        self.leading_coefficient = ttk.Entry(self)
        self.leading_coefficient.grid(row=1, column=1)
        self.second_coefficient = ttk.Entry(self)
        self.second_coefficient.grid(row=2, column=1)
        self.third_coefficient = ttk.Entry(self)
        self.third_coefficient.grid(row=3, column=1)
        self.constant_term = ttk.Entry(self)
        self.constant_term.grid(row=4, column=1)
        self.x_value = ttk.Entry(self)
        self.x_value.grid(row=5, column=1)
        self.results = ttk.Label(self, text="")
        self.results.grid(row=6, column=1)

    def calculate_y(self):
        a = float(self.leading_coefficient.get())
        b = float(self.second_coefficient.get())
        c = float(self.third_coefficient.get())
        d = float(self.constant_term.get())
        x = float(self.x_value.get())
        y = round((a*(x**3))+(b*(x**2))+(c*x)+d, 2)
        self.results.config(text="Y = " + str(y))

    def calculate_intercepts(self):
        a = float(self.leading_coefficient.get())
        b = float(self.second_coefficient.get())
        c = float(self.constant_term.get())
        d = float(self.third_coefficient.get())
        # y_int = round(a*(0**3))+(b*(0**2)+(c*0)+d, 2)
        x = 0
        while x < 3:
            x += .1
            y = (a*(x**3))+(b*(x**2))+(c*x)+d
            if y == 0:
                return x
            break

        self.results.config(text="X Int: " + str(x))

    def clear(self):
        self.leading_coefficient.delete(0, tk.END)
        self.second_coefficient.delete(0, tk.END)
        self.third_coefficient.delete(0, tk.END)
        self.constant_term.delete(0, tk.END)
        self.x_value.delete(0, tk.END)
        self.results.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    function_calculator(root)
    # root.geometry("500x500")
    root.title("Derek Haskell's Polynomial Calculator")
    root.mainloop()
