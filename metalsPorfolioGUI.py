# metals_gui.py
''' A tkinter program to track a portfolio of metals.
    Update spot prices of metals
    Update portfolio with purchases'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import json

#local imports
import file

# Common Variables such as file names
f_prices = "prices.json"
f_portfolio = "portfolio.json"


# root window
root = tk.Tk()
root.geometry('300x480')
root.resizable(True, True)
root.title('Metals Portfolio')
#
# Root window seems to be created here and mostly defined below.
# Is this the Define Root Window and below Define Widgets for Root Window?
#

# ttk styling for buttons
style = ttk.Style()
style.configure('TButton', foreground='black', relief='RAISED', padding=5)
boldStyle = ttk.Style()
style.configure("TButton", font = ('Sans','8','bold'))


# Functions for calculations go here
# Calculations:
#   1 ozt = 31.1 gr
#   1 oz  = 28.25 gr
#   1 gr = .0322 ozt
#   1 gr = .0353 oz

# Define the conversion rate based on gram or oz and metal type
# The rates take into account the gr to oz or ozt based on the metal type
# Dimes contain .0715 Troy ounces- Quarters .17875 OZT- Halfs .3575 ozt - dollars .7734 ozt
metal_conv_gr = {'sdime' : .0715,
                'sqtr' : .17875,
                'shdlr' : .3575,
                'sdlr' : .7734,
                'gold' : .0322,
                'sbar' : .0322,
                'cpr' : .0353}

metal_conv_oz = {'sdime' : .0715,
                'sqtr' : .17875,
                'shdlr' : .3575,
                'sdlr' : .7734,
                'gold' : 1,
                'sbar' : 1,
                'cpr' : 1}

selected_weight = tk.StringVar()
weighttype = (
    ('Grams', 'grams'),
    ('Ounces', 'oz'))

selected_metal = tk.StringVar()
metaltype = (
    ('Dime', 'sdime'),
    ('Quarter', 'sqtr'),
    ('Half Dollar', 'shdlr'),
    ('Dollar', 'sdlr'),
    ('Gold bullion', 'gold'),
    ('Silver bullion', 'sbar'),
    ('Copper bullion', 'cpr'))

def add_purchase():
    # calculate new total for metal purchased based on OZT for gold & silver, OZ for copper
    # if grams use gr_conversion table above to covert to oz(t) otherwise use oz_conversion table   
    if selected_weight.get() == "grams":              
        purchase = float(e_qty.get()) * metal_conv_gr[selected_metal.get()]
        print(f'Purchase is: {e_qty.get()} {selected_weight.get()} of {selected_metal.get()} ({purchase} oz)')
    else:
        purchase = float(e_qty.get()) * metal_conv_oz[selected_metal.get()]
        print(f'Purchase: {e_qty.get()} {selected_weight.get()} of {selected_metal.get()} is {purchase}')

    if selected_metal.get() == "gold":
        # read json file, add purchase to the selected metal 
        portfolio = file.read_json_file(f_portfolio)
        gtl = portfolio["Gold"]                       # read portfolio and get current gold total
        ngtl = portfolio["Gold"] + purchase           # new gold total
        txt = f'Gold tl: {gtl} + {purchase} = {ngtl}' 
        print(txt)                                    # log the changes for testing
        portfolio.update({"Gold":ngtl})               # add purchace to gold in portfolio
        file.save_json_file(f_portfolio, portfolio)   # save_json_file(file_nm, content)
    elif selected_metal.get() == "cpr":
        portfolio = file.read_json_file(f_portfolio)
        ctl = portfolio["Copper"]       
        nctl = portfolio["Copper"] + purchase         
        txt = f'Copper tl: {ctl} + {purchase} = {nctl}' 
        print(txt)                                    
        portfolio.update({"Copper":nctl})             
        file.save_json_file(f_portfolio, portfolio)   
    else:
        portfolio = file.read_json_file(f_portfolio)
        stl = portfolio["Silver"]                      
        nstl = portfolio["Silver"] + purchase           
        txt = f'Siver tl: {stl} + {purchase} = {nstl}' 
        print(txt)                                     
        portfolio.update({"Silver":nstl})              
        file.save_json_file(f_portfolio, portfolio)   
        # could add elif to check if in a list of siver sdime to sbar 
        # then create an error msg if it makes it to else


# GUI components

#  Child Window - Totals -----------------------------------------------------------------------
def totals_popup():
    totals = tk.Toplevel(root)
    totals.geometry("250x350")
    totals.title("Totals")
    #
    # Need to code file access to get totals, then remove showTotals function
    #
    portfolio = file.read_json_file(f_portfolio)
    gtl = portfolio["Gold"]
    stl = portfolio["Silver"]
    ctl = portfolio["Copper"]
    gtxt = f"Gold total is  : {gtl} TOZ"
    stxt = f"Silver total is: {stl} TOZ"
    ctxt = f"Copper total is: {ctl}  OZ"
    tk.Label(totals, text=gtxt).pack(fill='x', padx=5, pady=15)
    tk.Label(totals, text=stxt).pack(fill='x', padx=5, pady=15)
    tk.Label(totals, text=ctxt).pack(fill='x', padx=5, pady=15)
    
# End of Child Window - Totals -----------------------------------------------------------------


# Child Window - Update
def update_popup():
    updt= tk.Toplevel(root)
    updt.geometry("250x350")
    updt.title("Update Spot Prices")
    tk.Label(updt, text="Select metal to update spot price on").pack(fill='x', padx=5, pady=15)
    #
    # Need to code file access to get totals, then remove showTotals function
    #
    #tk.Label(top, text= gtxt).pack(padx=5, pady=5, side=tk.TOP)
    print("Updating prices...")

# End of Child Window - Update -----------------------------------------------------------------


# Root Window ----------------------------------------------------------------------------------

#   label
labelAdd = ttk.Label(text="Enter quantity")
labelAdd.pack(fill='x', padx=5, pady=15)

e_qty = tk.Entry(root)
e_qty.pack(fill='x', padx=5, pady=5)

#   label
labelweight = ttk.Label(text="Select weight (grams / ounces)",
            borderwidth=2, 
            relief="raise", 
            background="light gray")
labelweight.pack(fill='x', padx=5, pady=15)

#   radio buttons for weight type

for weight in weighttype:
    rb_weight = ttk.Radiobutton(
        root,
        text=weight[0],
        value=weight[1],
        variable=selected_weight)
    rb_weight.pack(fill='x', padx=5)


#   label
labelmetal = ttk.Label(text=" Select purchace type", 
            borderwidth=2, 
            relief="raise", 
            background="light gray")
labelmetal.pack(fill='x', padx=5, pady=15)

#   radio buttons for metal type

for metal in metaltype:
    rb_metal = ttk.Radiobutton(
        root,
        text=metal[0],
        value=metal[1],
        variable=selected_metal)
    #rb_metal.pack(fill='x', padx=5, pady=5)
    rb_metal.pack(fill='x', padx=5)

#   button
buttonAdd = ttk.Button(root,
            text="Add Purchase",
            style='TButton',
            command=add_purchase)
buttonAdd.pack(fill='x', padx=5, pady=5)

#   button
buttonShow = ttk.Button(
    root,
    text="Show Totals",
    command=totals_popup)
buttonShow.pack(padx=5, pady=5, side=tk.LEFT)

#   button
buttonUpdate = ttk.Button(
    root,
    text="Update Spot Price",
    command=update_popup)
buttonUpdate.pack(padx=5, pady=5, side=tk.RIGHT)

# End of Root Window ---------------------------------------------------------------------------


# Main Program ---------------------------------------------------------------------------------

root.mainloop()