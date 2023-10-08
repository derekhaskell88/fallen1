import tkinter as tk
from tkinter import ttk, messagebox


class inventory_game(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.inventory = ["potion", "dagger", "cloak"]

        self.display = ttk.Label(parent, text="", padding="50 50 50 50")
        self.display.pack()
        ttk.Label(parent, text="Enter Command").pack()
        self.user_command = ttk.Entry(parent)
        self.user_command.pack()
        ttk.Label(parent, text="Enter Arg 1").pack()
        self.item_grab = ttk.Entry(parent)
        self.item_grab.pack()
        ttk.Label(parent, text="Enter Arg 2").pack()
        self.num_grab = ttk.Entry(parent)
        self.num_grab.pack()

        ttk.Button(parent, text="apply",
                   command=self.apply).pack()
        ttk.Label(parent, text="\nCommand List:\n\nshow - Shows Inventory: No Args\ngrab - Grabs an Item: Arg1 - Enter Item Name\nedit - Edits an Item: Arg1 - New Item Name, Arg2 Number to Edit\ndrop - Drops an Item: Arg2 Number to Drop\nexit - Exits Application: No Args").pack()

    def apply(self):
        user_command = self.user_command.get()
        inventory = self.inventory

        if user_command == "show":
            textvar = '\n'.join(
                [f"{number}. {item}" for number, item in enumerate(inventory, start=1)])
            self.display.config(
                text=textvar)
            self.user_command.delete(0, tk.END)
        elif user_command == "grab":
            self.user_command.delete(0, tk.END)

            if len(inventory) >= 4:
                self.display.config(text="You must drop an item first.")
                self.item_grab.delete(0, tk.END)
            else:
                item = self.item_grab.get()
                inventory.append(item)
                self.display.config(text=str(item) + " was added.")
                self.item_grab.delete(0, tk.END)
        elif user_command == "edit":
            number = int(self.num_grab.get())
            if number < 1 or number > len(inventory):
                self.display.config(text="Invalid item number.")
                self.num_grab.delete(0, tk.END)

            else:
                self.user_command.delete(0, tk.END)
                item = self.item_grab.get()
                inventory[number-1] = item
                self.display.config(
                    text=f"Item number {number} was updated.")
                self.item_grab.delete(0, tk.END)
                self.num_grab.delete(0, tk.END)
        elif user_command == "drop":
            number = int(self.num_grab.get())
            if number < 1 or number > len(inventory):
                self.display.config(text="Invalid item number.")
                self.num_grab.delete(0, tk.END)
            else:
                self.user_command.delete(0, tk.END)
                item = inventory.pop(number-1)
                self.display.config(text=f"{item} was dropped.")
                self.num_grab.delete(0, tk.END)
        elif user_command == "exit":
            root.destroy()
        else:
            self.display.config(text="Please Enter a Valid Command")


if __name__ == "__main__":
    root = tk.Tk()
    inventory_game(root)
    root.geometry("500x500")
    root.title("Derek Haskell's Wizard Inventory Game")
    root.mainloop()
