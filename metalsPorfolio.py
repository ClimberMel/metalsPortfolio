# metalsPortfolio.py


# Imported Modules --------------------------------------------------------------------------
import json


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

#def readPortfolio()
#    with open('metals.csv', 'r') as f:
#        metals = csv.reader(f, delimiter=',')
#    print(metals)
#    f.close

def getPrices():
    prices = {"Gold_OZT" : 1806.7, "Silver_OZT" : 22.56, "Copper_OZ" : .27}
    return prices

def savePrices(prices):
    pricesFile = "prices.json"
    with open(pricesFile, 'w') as f: 
        json.dump(prices, f)

def readPrices():
    pricesFile = "prices.json"
    with open(pricesFile) as f: 
        prices = json.load(f) 
        return prices

def readPortfolio():
    portfolioFile = "portfolio.json"
    with open(portfolioFile) as f: 
        portfolio = json.load(f) 
        return portfolio        

def main():

    border = "**************************************"




# Main Program ---------------------------------------------------------------------------
#   I haven't set up the portfolio file yet

# run the following two lines once to create prices file
#prices = getPrices()
#savePrices(prices)

prices = readPrices()

print(prices["Gold_OZT"])

prices.update({"Gold_OZT":2207.85})

print(prices["Gold_OZT"])

# This will save the updated price to the file
savePrices(prices)

