import tkinter as tk
from tkinter import ttk, messagebox
import math


class function_calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)
        self.display = tk.StringVar()
        self.display_entry = ttk.Entry(
            parent, textvariable=self.display, state="readonly")
        self.display_entry.pack()


if __name__ == "__main__":
    root = tk.Tk()
    function_calculator(root)
    root.geometry("500x500")
    root.title("Derek Haskell's Polynomial Calculator")
    root.mainloop()
