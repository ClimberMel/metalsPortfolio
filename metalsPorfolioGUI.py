# groceryCalcGUI.py

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('500x400')
root.resizable(True, True)
root.title('Metals Portfolio')


# Functions for calculations go here


# Functions for file handling go here

def add_purchase():
    # pass purchace here
    print('Purchace added')
    # calculate new total for metal purchased


# GUI components

selected_weight = tk.StringVar()
weighttype = (('Grams', 'grams'),
        ('Troy Ounces', 'ozt'))

selected_metal = tk.StringVar()
metaltype = (('Dime', 'sdime'),
        ('Quarter', 'sqtr'),
        ('Half Dollar', 'shdlr'),
        ('Dollar', 'sdlr'),
        ('Gold bullion', 'gold'),
        ('Silver bullion', 'slvr'))


# label
labelAdd = ttk.Label(text="Enter quantity")
labelAdd.pack(fill='x', padx=5, pady=15)

e_qty = tk.Entry(root)
e_qty.pack(fill='x', padx=5, pady=5)

# label
labelweight = ttk.Label(text="Select weight (grams / ounces)")
labelweight.pack(fill='x', padx=5, pady=15)

# radio buttons for weight type

for weight in weighttype:
    rb_weight = ttk.Radiobutton(
        root,
        text=weight[0],
        value=weight[1],
        variable=selected_weight)
    rb_weight.pack(fill='x', padx=5, pady=5)


# label
labelmetal = ttk.Label(text="Select purchace type")
labelmetal.pack(fill='x', padx=5, pady=15)

# radio buttons for metal type

for metal in metaltype:
    rb_metal = ttk.Radiobutton(
        root,
        text=metal[0],
        value=metal[1],
        variable=selected_metal)
    #rb_metal.pack(fill='x', padx=5, pady=5)
    rb_metal.pack(fill='x', padx=5)

# button
button = ttk.Button(
    root,
    text="Add Purchase",
    command=add_purchase)
button.pack(fill='x', padx=5, pady=5)

root.mainloop()