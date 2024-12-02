# Import cars data
import pandas as pd
cars = pd.read_csv('02_Intermediate_Python/Dictionaries & Pandas/Pandas/cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])
print()

# Print out fourth, fifth and sixth observation
print(cars[3:6])
print()