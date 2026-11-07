# Reflection Questions

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

    