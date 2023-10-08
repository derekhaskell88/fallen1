
import tkinter as tk
from tkinter import ttk

# create the main window
root = tk.Tk()
root.geometry('100x100')

# create the calculator screen
screen = ttk.Frame(root, width=100, height=100)
screen.pack(fill=tk.BOTH, expand=True)

# create a label for the calculator screen with a black outline
label = ttk.Label(screen, text='', font=('Helvetica', 12),
                  width=50, height=50, borderwidth=2, relief='solid')
label.pack(side=tk.TOP, pady=10)

# start the event loop
root.mainloop()
