prices = [100, 200, 300]
quantities = [2, 1, 3]
discount = 10
tax = 5

total = sum(p * q for p, q in zip(prices, quantities))
total -= total * discount / 100
total += total * tax / 100

print("Total cost:", total)
