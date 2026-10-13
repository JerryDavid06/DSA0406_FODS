import pandas as pd

order_data = pd.DataFrame({
    "Customer": [1, 2, 1, 3],
    "Date": ["2026-01-05", "2026-01-03",
             "2026-01-08", "2026-01-10"],
    "Product": ["Pen", "Book", "Pen", "Book"],
    "Quantity": [2, 3, 4, 1]
})

order_data["Date"] = pd.to_datetime(order_data["Date"])

print("Orders per customer:")
print(order_data.groupby("Customer").size())
print("\nAverage quantity per product:")
print(order_data.groupby("Product")["Quantity"].mean())
print("\nEarliest order:", order_data["Date"].min())
print("Latest order:", order_data["Date"].max())
