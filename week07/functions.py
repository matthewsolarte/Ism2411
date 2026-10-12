# --- Exercise 1 ---

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")  # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}")  # 20.00
print(f"Another tax: ${calculate_tax(150, 0.05):.2f}")  # 7.50

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


# Calling the function
price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# --- Exercise 3 ---

# Write it out manually first, then refactor to use a function

discount = apply_discount(200, "gold")  # used below
tax = calculate_tax(discount, 0.07)
after_tax = discount + tax
print(f"After gold discount: ${discount:.2f}")
print(f"After tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Final price for ${price} order with {tier} tier: ${total:.2f}")


# --- Exercise 5 ---

x = 100 # apple

def double_it(x):

    # x = 999 # local another apple (not the same apple as above)
    return x * 2

print(x)
print(double_it(x))
print(x)

# --- Module 08 Reflection ---

# 1. git log --oneline output:
# 321edc1 add README with module listing and run instructions
# b1babed add module 7 functions: calculate_tax, apply_discount, final_price
# 80e3fe3 add .gitignore for Python and OS files
# 7784144 Initial commit

#
# This history shows small, separate commits with clear messages. If I were
# hiring, it would tell me this person works in organized steps, sets up the
# project before adding code, and documents what they do.

# 2. Git changes how I edit a working script. Before, I would copy the file
# and rename it final2 or backup. Now I can make one small change, test it,
# and commit it, knowing I can always go back to a version that worked.

# 3. I would add my virtual environment folder, venv/, to .gitignore. It is
# large, it is specific to my machine, and anyone can rebuild it from a
# requirements file, so it should not be tracked.