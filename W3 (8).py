n = int(input("Enter number of prices: "))

prices = []

for i in range(n):
    price = int(input(f"Enter price {i+1}: "))
    prices.append(price)

total_sum = sum(prices)

product = 1
for price in prices:
    product *= price

average = total_sum / n

print("SUM =", total_sum)
print("PRODUCT =", product)
print("AVERAGE =", average)
