import numpy as np

sales_data = np.array([10000, 12000, 15000, 18000])

total = np.sum(sales_data)
increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total annual sales:", total)
print("Percentage increase:", increase, "%")
