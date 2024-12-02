# Import cars data
import pandas as pd
cars = pd.read_csv('02_Intermediate_Python/Dictionaries & Pandas/Pandas/cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'cars_per_cap'])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'], ['country', 'drives_right']])