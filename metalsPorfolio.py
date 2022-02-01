# metalsPortfolio.py


# Imported Modules --------------------------------------------------------------------------

# For the GUI -------------------------------------------------------------------------------
    # import tkinter as tk
    # from tkinter import ttk
    # from tkinter.messagebox import showinfo

# For displaying data in a dataframe --------------------------------------------------------
    # import pandas as pd
    # from pandas_datareader import data as web

    # import plotly.graph_objects as go

# Possibly numpy fo calcualations     --------------------------------------------------------
    # import numpy as np



# Defined classes  --------------------------------------------------------------------------

    # none yet

# Defined modules  --------------------------------------------------------------------------

def readPortfolio()
    with open('metals.csv', 'r') as f:
        metals = csv.reader(f, delimiter=',')
    print(metals)
    f.close

def main():

    border = "**************************************"
    readPortfolio()
    print('You have a portfolio called metals')
    print('Now you need to add to it and calculate it's value')


# Main Program ---------------------------------------------------------------------------
main()