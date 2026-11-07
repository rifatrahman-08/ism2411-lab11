# Reflection Questions
# 1. I would use .get() when a key might be missing so my code does not crash. I would use bracket notation when I know the key exists and need its value. My rule is to use .get() when I am not sure the key exists.
# 2. Exercise 8 reminds me of using SUMIF in Excel to add numbers based on a group. Python can do this faster with large datasets because it can process many records automatically.

# Exercise 1
customer = {
    "name": "Alice", # Key : Value ,
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}


print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

# Exercise 2
customer["phone"] = '555-5555'
print(customer)
customer["tier"] = 'platinum'
print(customer)
del customer["Name"]
print(customer)


print(customer.get("ytd_spend",0))

# Exercise 3


print(customer.get("email", "no email on file"))

# Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")


for something in customer:
    print(something, customer[something])

# Exercise 5:
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}


purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

# Exercise 6
dict1 = {"name": "Reed", "tier": "platinum"}
dict2 = {"name": "Markum", "tier": "gold"}
dict3 = {"name": "John", "tier": "silver"}

customers = [dict1, dict2, dict3]

for customer in customers:
    tier = customer["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{customer['name']}: {tier}, Discount: ${discount_amount:.2f}")

# Exercise 7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}


for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} - only {details['stock']} left")


# Exercise 8

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]


sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount


print(sales_by_region)


for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")
