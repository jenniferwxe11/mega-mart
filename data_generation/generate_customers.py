import random
import uuid

import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CUSTOMERS = 100

customers = []
customer_ids = []

for _ in range(NUM_CUSTOMERS):
    cid = str(uuid.uuid4())
    customer_ids.append(cid)

    name = fake.name()

    # email with incorrect format or whitespace
    email = fake.email()
    if random.random() < 0.1:
        email = email.replace('@',' ')
    if random.random() < 0.15:
        email = ' ' + email

    # inconsistent gender labelling
    gender = random.choice([
        'Male',
        'Female',
        'f',
        'm',
        'male',
        'female',
        ''
        ])
    
    dob = fake.date_of_birth(minimum_age = 18, maximum_age = 85)

    # loyalty points with mixed data types
    loyalty_points = random.choice([random.randint(0,10000), 'N/A', True])

    # sign up date with inconsistent format
    signup_date = fake.date_between(start_date='-3y', end_date='today')
    formats = ['%Y-%m-%d', '%d/%m/%Y', '%b %d, %Y']
    signup_date = signup_date.strftime(random.choice(formats))
        
    customers.append({
        "customer_id": cid,
        "name": name,
        "email": email,
        "gender": gender,
        "dob": dob,
        "loyalty_points": loyalty_points,
        "signup_date": signup_date
    })

# duplicates with minor variations
for _ in range(5):
    cust = random.choice(customers).copy()
    cust["customer_id"] = str(uuid.uuid4())
    cust["name"] = cust["name"].replace('a','4')
    cust["email"] = cust["email"].strip().lower()
    customers.append(cust)


df_customers = pd.DataFrame(customers)
df_customers.to_csv("customers_raw.csv",index=False)
print("customers_raw.csv file generated")