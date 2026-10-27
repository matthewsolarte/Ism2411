# Reflection
#
# 1. What surprised me most about lists in Python:
#    I expected lists to be fixed like a row in Excel, but they can grow and
#    shrink at any time with append and remove. Negative indexes also surprised
#    me, since inventory[-1] gets the last item without knowing the length.
#    Slicing with a step like [::2] was new too, it pulls every other item in one line.
#
# 2. A business situation where a list would have saved time:
#    In a finance class we had a column of daily sales and had to find the total,
#    the average, and only the days above a target. In Excel that meant writing
#    several formulas and filters by hand. With a Python list, sum(), len(), max(),
#    min(), and one loop with an if statement do all of it at once, and the same
#    code works again next week with new numbers.


# Exercise 1: Build the list
print("--- Exercise 1 ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# Exercise 2: Index practice
print("\n--- Exercise 2 ---")
print(inventory[0])                     # first item
print(inventory[-1])                    # last item
middle = len(inventory) // 2
print(inventory[middle])                # middle item, computed from len()


# Exercise 3: Slicing
print("\n--- Exercise 3 ---")
print(inventory[:3])                    # first three
print(inventory[-2:])                   # last two
print(inventory[::2])                   # every other item


# Exercise 4: Modify
print("\n--- Exercise 4 ---")
inventory.append("envelope")
print("After append:", inventory)
inventory.remove("tape")
print("After remove:", inventory)
inventory.sort()
print("After sort:", inventory)


# Exercise 5: Tuple comparison
print("\n--- Exercise 5 ---")
coords = (40.7128, -74.0060)            # NYC latitude and longitude
try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples cannot be changed after they are created. That is useful for "
          "coordinates because a location should stay fixed and never be "
          "changed by accident.")
print(coords)


# Exercise 6: Average of a list of sales
print("\n--- Exercise 6 ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7: Accumulator pattern
print("\n--- Exercise 7 ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print("Original:  ", prices)
print("Discounted:", discounted)


# Exercise 8: Filter above threshold
print("\n--- Exercise 8 ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for day in sales:
    if day > 300:
        high_sales.append(day)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
