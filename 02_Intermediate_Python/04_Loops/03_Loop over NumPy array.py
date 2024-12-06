"""
Import the numpy package under the local alias np.

Write a for loop that iterates over all elements in np_height and 
prints out "x inches" for each element, where x is the value in the array.

Write a for loop that visits every element of the np_baseball array and prints it out.
"""

# Import numpy as np
import numpy as np 

np_height = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69, 70, 73, 75 ]
np_baseball = [[74, 180], [74, 215], [72, 210], [72, 210], [73, 188], [69, 176]]
                

# For loop over np_height
for x in np.nditer(np_height):
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(str(x))