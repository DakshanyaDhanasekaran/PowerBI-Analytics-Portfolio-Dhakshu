import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

# Parameters
num_rows = 1200

regions = ["North", "South", "East", "West"]
cities = ["Chennai", "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Kolkata"]
categories = {
    "Electronics": ["Mobile", "Laptop", "Headphones", "TV"],
    "Clothing": ["Shirt", "Jeans", "Jacket", "Dress"],
    "Furniture": ["Sofa", "Table", "Chair", "Bed"],
    "Grocery": ["Rice", "Oil", "Milk", "Snacks"]
}
payment_modes = ["UPI", "Card", "Cash", "Net Banking"]
genders = ["Male", "Female"]

data = []

start_date = datetime(2023, 1, 1)

for i in range(1, num_rows + 1):
    category = random.choice(list(categories.keys()))
    subcategory = random.choice(categories[category])
    quantity = np.random.randint(1, 6)
    unit_price = np.random.randint(100, 5000)
    discount = round(np.random.uniform(0, 0.3), 2)
    revenue = quantity * unit_price * (1 - discount)
    cost = revenue * np.random.uniform(0.6, 0.9)
    profit = revenue - cost
    
    data.append([
        i,
        start_date + timedelta(days=np.random.randint(0, 365)),
        random.choice(regions),
        random.choice(cities),
        category,
        subcategory,
        f"CUST{np.random.randint(1000, 2000)}",
        np.random.randint(18, 60),
        random.choice(genders),
        quantity,
        unit_price,
        discount,
        round(revenue, 2),
        round(profit, 2),
        random.choice(payment_modes)
    ])

columns = [
    "OrderID", "OrderDate", "Region", "City", "Category", "SubCategory",
    "CustomerID", "CustomerAge", "Gender", "Quantity",
    "UnitPrice", "Discount", "Revenue", "Profit", "PaymentMode"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("sales_analytics_dataset.csv", index=False)

print("CSV file generated successfully!")