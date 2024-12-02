# Import cars data
import pandas as pd
cars = pd.read_csv('02_Intermediate_Python/Dictionaries & Pandas/Pandas/cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])
print()

# Print out country column as Pandas DataFrame
print(cars[['country']])
print()

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])