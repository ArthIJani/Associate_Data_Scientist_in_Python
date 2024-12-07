"""
Write a for loop that iterates over the rows of cars and on 
each iteration perform two print() calls: one to print out the row label 
and one to print out all of the rows contents.
"""

# Import cars data
import pandas as pd
cars = pd.read_csv('02_Intermediate_Python/04_Loops/cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)