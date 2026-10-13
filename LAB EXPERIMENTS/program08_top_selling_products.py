import pandas as pd

data = pd.DataFrame({
    "Product": ["Pen", "Book", "Pen", "Bag", "Book"],
    "Quantity": [10, 5, 15, 8, 12]
})

top_products = data.groupby("Product")["Quantity"].sum().nlargest(5)
print("Top-selling products:")
print(top_products)
