import random
import uuid

import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_PHYSICAL_STORES = 10

stores = []
store_ids = []

regions = ["Central", "North", "South", "East", "West"]

for _ in range(NUM_PHYSICAL_STORES):
    sid = str(uuid.uuid4())
    store_ids.append(sid)

    stores.append({
        "store_id": sid,
        "store_name": f"MegaMart {fake.city()}",
        "location": fake.address().replace('\n',', '),
        "region": random.choice(regions),
        "store_type": "Physical Store"
    })

stores.append({
    "store_id": str(uuid.uuid4()),
    "store_name": "MegaMart Online",
    "location": "Online",
    "region": "Nationwide",
    "store_type": "Online Website"
})

stores.append({
    "store_id": str(uuid.uuid4()),
    "store_name": "MegaMart App",
    "location": "Online",
    "region": "Nationwide",
    "store_type": "Mobile App"
})

df_stores = pd.DataFrame(stores)
df_stores.to_csv("data_generation/raw_data/stores_raw.csv", index=False)
print("stores_raw.csv file generated")