import matplotlib.pyplot as plt 

year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
pop =  [2.5, 2.6, 2.8, 3.0, 3.1, 4.0, 6.5, 7.5, 8.0, 8.3, 8.4, 8.8, 8.9, 9.0, 9.5, 10.0]

# Add More Data
year = [1800, 1850, 1900] + year
pop = [1.0, 1.5, 2.0] + pop

plt.plot(year, pop)

# Labels
plt.xlabel('Year')
plt.ylabel('Population')

# Title Label
plt.title("World Population Projections")

# Ticks
plt.yticks([0, 2, 4, 6, 8, 10],['0', '2B', '4B', '6B', '8B', '10B'])

plt.show()