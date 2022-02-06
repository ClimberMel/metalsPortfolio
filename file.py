# file.py
'''File handling module for reading and writing to a json file'''

import json

# Pass the file name and then it can read both prices and portfolio files with one function

# This was only to create the file.  It could eventually be automated to get the 
# spot prices from the web and save them
def get_prices():
    prices = {"Gold_OZT" : 1806.7, "Silver_OZT" : 22.56, "Copper_OZ" : .27}
    return prices

# Pass a file name to read_json_file and it will return the content
def read_json_file(file_nm):
    this_file = file_nm
    with open(this_file) as f: 
        contents = json.load(f) 
        f.close()
        return contents

# Pass a file name and content to save_json_file and it will save the content to the file name
def save_json_file(file_nm, content):
    this_file = file_nm
    this_content = content
    with open(this_file, 'w') as f: 
        json.dump(this_content, f)
        f.close()


