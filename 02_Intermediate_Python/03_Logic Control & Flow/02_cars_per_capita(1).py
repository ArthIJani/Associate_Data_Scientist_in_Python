"""
Remember about np.logical_and(), np.logical_or() and np.logical_not(), 
the NumPy variants of the and, or and not operators? 
You can also use them on Pandas Series to do more advanced filtering operations.

Take this example that selects the observations that have a cars_per_cap 
between 10 and 80. Try out these lines of code step by step to see what's happening.

Use the code sample provided to create a DataFrame medium, 
that includes all the observations of cars that have 
a cars_per_cap between 100 and 500.

Print out medium.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('02_Intermediate_Python/03_Logic Control & Flow/cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)