import random
import uuid
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_TRANSACTIONS = 500

transactions = []
transaction_ids = []

customers_df = pd.read_csv("data_generation/raw_data/customers_raw.csv")
customer_ids = customers_df["customer_id"].dropna().tolist()

products_df = pd.read_csv("data_generation/raw_data/products_raw.csv")
product_ids = products_df["product_id"].dropna().tolist()

stores_df = pd.read_csv("data_generation/raw_data/stores_raw.csv")
store_ids = stores_df["store_id"].dropna().tolist()

for _ in range(NUM_TRANSACTIONS):
    transaction_id = str(uuid.uuid4())
    transaction_ids.append(transaction_id)
    customer_id = random.choice(customer_ids + [None,""])
    product_id = random.choice(product_ids + [None,""])
    store_id = random.choice(store_ids + [None,""])

    price = random.choices(
        [round(random.uniform(5,300),2), 0.0, -10.0, None, ""],
        weights = [0.85, 0.05, 0.03, 0.04, 0.03],
        k = 1
    )[0]

    quantity = random.choices(
        [random.randint(1,5), 0, -2, None, ""],
        weights = [0.85, 0.05, 0.03, 0.04, 0.03],
        k = 1
    )[0]

    try:
        subtotal = float(price) * int(quantity)
    except:
        subtotal = None
    
    if subtotal is not None and random.random() > 0.2:
        total_amount = round(subtotal,2)
    elif subtotal is None:
        total_amount = None
    else:
        error_type = random.choices(
            ["slight","big","null"],
            weights = [0.5, 0.3, 0.2],
            k = 1
            )[0]
        
        if error_type == "slight":
            total_amount = round(round(subtotal,2) * random.uniform(0.9,1.1),2)
        elif error_type == "big":
            total_amount = round(random.uniform(5,500),2)
        else:
            total_amount = None

    date = fake.date_between(start_date = "-1y", end_date = "+30d") if random.random() > 0.05 else ""

    payment_method = random.choice(["Credit Card",
                                    "CREDIT_CARD",
                                    "Cash",
                                    "",
                                    None])
    
    transactions.append({
        "transaction_id": transaction_id,
        "customer_id": customer_id,
        "product_id": product_id,
        "store_id": store_id,
        "date": date,
        "quantity": quantity,
        "price": price,
        "total_amount": total_amount,
        "payment_method": payment_method
    })

df_transactions = pd.DataFrame(transactions)
df_transactions.to_csv("data_generation/raw_data/transactions_raw.csv",index=False)
print("transactions_raw.csv file generated")
