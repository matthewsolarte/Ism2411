# Reflection
#
# 1. The most surprising thing about lists was how easy they are to change.
#    I can add, remove, and sort items with one line each, like append, remove,
#    and sort. I also did not expect negative indexes, where list[-1] gives the
#    last item without knowing how long the list is.
#
# 2. For Solartech Logistics I compared Kenworth T680 truck prices from
#    Ritchie Bros. auctions. I put the prices in Excel and had to write separate
#    formulas for the average, the lowest price, and a filter for trucks under
#    my budget. With a Python list, sum(), len(), min(), and one loop would do
#    all of that at once, and I could reuse the same code every time new
#    auctions came out.


# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# Exercise 2
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])


# Exercise 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)


# Exercise 5
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError, tuples cannot be changed.")
    print("This is useful for coordinates because a location should never change by accident.")
print(coords)


# Exercise 6
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)


# Exercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for day in sales:
    if day > 300:
        high_sales.append(day)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
