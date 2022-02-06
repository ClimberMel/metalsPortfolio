# groceryCalcGUI.py

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import json

# root window
root = tk.Tk()
root.geometry('300x480')
root.resizable(True, True)
root.title('Metals Portfolio')


# Functions for calculations go here

def totals_popup():
    top= tk.Toplevel(root)
    top.geometry("250x350")
    top.title("Totals")
    #
    # Need to code file access to get totals, then remove showTotals function
    #
    gtxt = "Total Gold is  : %s OZT"%str(tl[0])
    stxt = "Total Silver is: %s OZT"%str(tl[1])
    ctxt = "Total Copper is: %s OZ"%str(tl[2])
    #tk.Label(top, text= gtxt).pack(padx=5, pady=5, side=tk.TOP)
    tk.Label(top, text= gtxt).grid(column="0", row="0")
    tk.Label(top, text= stxt).grid(column="0", row="1")
    tk.Label(top, text= ctxt).grid(column="0", row="2")

def add_purchase():
    # pass purchace here
    # Dimes contain .0715 Troy ounces- Quarters .17875 OZT- Halfs .3575 ozt - dollars .7734 ozt
    print(e_qty.get())
    print(selected_weight.get())
    print(selected_metal.get())
    # calculate new total for metal purchased
    print(f'Purchase: {e_qty.get()} {selected_weight.get()}s of {selected_metal.get()}')

    # save updated totals to file
    # call saveFile('portfolio.json')


# Functions for file handling go here
#   Perhaps pass the file name and then it can read both prices and portfolio files with one function
def readPrices():
    pricesFile = "prices.json"
    with open(pricesFile) as f: 
        prices = json.load(f) 
        return prices



def updatePrices():
    prices = readPrices()
    prices.update({"Gold_OZT":2207.85})

#   Pass the file name and then it can write either prices or portfolio files with one function
def saveFile(file):
    pass


# GUI components

selected_weight = tk.StringVar()
weighttype = (('Coins', 'coin'),
        ('Grams', 'grams'),
        ('Ounces', 'oz'))

selected_metal = tk.StringVar()
metaltype = (('Dime', 'sdime'),
        ('Quarter', 'sqtr'),
        ('Half Dollar', 'shdlr'),
        ('Dollar', 'sdlr'),
        ('Gold bullion', 'gold'),
        ('Silver bullion', 'slvr'),
        ('Copper bullion', 'cpr'))


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
    rb_weight.pack(fill='x', padx=5)


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
buttonAdd = ttk.Button(
    root,
    text="Add Purchase",
    command=add_purchase)
buttonAdd.pack(fill='x', padx=5, pady=5)

# button
buttonShow = ttk.Button(
    root,
    text="Show Totals",
    command=totals_popup)
buttonShow.pack(padx=5, pady=5, side=tk.LEFT)

# button
buttonUpdate = ttk.Button(
    root,
    text="Update Spot",
    command=updatePrices)
buttonUpdate.pack(padx=5, pady=5, side=tk.RIGHT)


root.mainloop()