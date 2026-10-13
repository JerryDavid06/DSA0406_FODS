import pandas as pd

property_data = pd.DataFrame({
    "Location": ["Chennai", "Delhi", "Chennai", "Mumbai"],
    "Bedrooms": [3, 5, 6, 2],
    "Area": [1200, 2000, 2500, 1000],
    "Price": [5000000, 8000000, 10000000, 4000000]
})

print("Average listing price by location:")
print(property_data.groupby("Location")["Price"].mean())

print("\nProperties with more than four bedrooms:",
      (property_data["Bedrooms"] > 4).sum())

print("\nProperty with the largest area:")
print(property_data.loc[property_data["Area"].idxmax()])
