import random
import uuid

import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_PRODUCTS = 50

# price inconsistent data type
def random_price():
    return round(random.uniform(5,300),2) if random.random() > 0.05 else "free"

products = []
product_ids = []

for _ in range(NUM_PRODUCTS):
    pid = str(uuid.uuid4())
    product_ids.append(pid)

    # product name with inconsistent casing, extra spaces or special characters
    name = fake.word().capitalize() + " " + fake.word()
    if random.random() < 0.1:
        name = " " + name.upper() + "!"

    # typos in category
    category = random.choice([
        "Groceries",
        "Electronics",
        "Electornics",
        "Fashion",
        "Fashon",
        "",
        None
    ])

    # inconsistent stock value
    stock = random.choices(
        population = [random.randint(1,1000),0, "No stock"],
        # 70% normal number, 20% zero, 10% "No stock"
        weights = [0.7, 0.2, 0.1],
        k = 1
    )[0]


    products.append({
        "product_id": pid,
        "name": name,
        "category": category,
        "price": random_price(),
        "stock": stock
    })

df_products = pd.DataFrame(products)
df_products.to_csv("products_raw.csv",index=False)
print("products_raw.csv file generated")