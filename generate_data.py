import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

rows = 15000

data = {
    "order_id": np.arange(1, rows+1),
    "timestamp": [datetime.now() - timedelta(minutes=i) for i in range(rows)],
    "region": np.random.choice(["North", "South", "East", "West"], rows),
    "category": np.random.choice(["Electronics", "Clothing", "Home", "Sports"], rows),
    "sales": np.random.randint(500, 5000, rows),
    "quantity": np.random.randint(1, 10, rows),
    "rating": np.round(np.random.uniform(1, 5, rows), 1)
}

df = pd.DataFrame(data)
df["profit"] = df["sales"] * np.random.uniform(0.1, 0.3, rows)

df.to_csv("large_sales_data.csv", index=False)

print("Dataset generated successfully!")