import numpy as np

# Columns: bedrooms, area, sale price
house_data = np.array([
    [3, 1200, 200000],
    [5, 1800, 350000],
    [6, 2200, 450000],
    [4, 1500, 250000]
])

houses = house_data[house_data[:, 0] > 4]
if len(houses) > 0:
    print("Average sale price:", np.mean(houses[:, 2]))
else:
    print("No houses have more than four bedrooms.")
