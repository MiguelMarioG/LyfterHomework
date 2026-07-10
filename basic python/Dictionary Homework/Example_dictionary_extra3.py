products = [
    {"name": "Monitor", "category": "Electronic", "price": 200},
    {"name": "Keyboard", "category": "Electronic", "price": 50},
    {"name": "Chair", "category": "furniture", "price": 120},
    {"name": "Table", "category": "furniture", "price": 180},
    {"name": "Mouse", "category": "Electronic", "price": 25},
]

totals_by_category = {}

for index in products:
    category = index["category"]
    price = index["price"]
    
    if category in totals_by_category:
        totals_by_category[category] += price
    else:
        totals_by_category[category] = price

print(totals_by_category)