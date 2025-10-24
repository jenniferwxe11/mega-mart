import random
import pandas as pd
from config import NUM_CUSTOMERS
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

customers = []
customer_ids = []

region_area_df = pd.read_csv("data_generation/raw_data/region_areas.csv")

def get_random_region_area():
    row = region_area_df.sample(n=1).iloc[0]
    region, area = row['region'], row['area']
    return region, area

dirty_rows = int(NUM_CUSTOMERS * 0.04)

for i in range(1, NUM_CUSTOMERS - dirty_rows + 1):
    cid = f"CUST{i:03d}"
    customer_ids.append(cid)

    # Customer type
    customer_type = random.choices(
        ["Retail Walk-In", "Retail Members", "Online Only", "Omnichannel"],
        weights = [0.6, 0.15, 0.15, 0.1],
        k = 1
    )[0]

    # Default values
    name = None
    email = None
    gender = None
    dob = None
    area = None
    region = None
    signup_date = None
    loyalty_points = None
    email_opt_in = None
    sms_opt_in = None
    push_opt_in = None
    walk_in_flag = False

    # Retail walk in
    if customer_type == "Retail Walk-In":
        walk_in_flag = True
    
    # Retail members
    elif customer_type == "Retail Members":
        email = f'{fake.user_name()}@{fake.safe_domain_name()}'
        signup_date = fake.date_between(start_date='-6M', end_date='today')
        loyalty_points = 0

    # Online only customers
    elif customer_type == "Online Only":
        first_name = fake.first_name()
        last_name = fake.last_name()
        name = first_name + " " + last_name
        email = f'{first_name}.{last_name}@{fake.safe_domain_name()}'.lower()
        # Inconsistent gender label
        gender = random.choices(
            ["Female", "Male", "f", "m", "F", "M", ""],
            weights = [0.4, 0.4, 0.05, 0.03, 0.05, 0.1, 0.05],
            k=1
            )[0]
        # area, region = get_random_singapore_area_region()
        dob = fake.date_of_birth(minimum_age = 18, maximum_age = 85)
        region, area = get_random_region_area()
        signup_date = fake.date_between(start_date='-6M', end_date='today')
        loyalty_points = 0

        email_opt_in = random.choices(
            [True, False],
            weights = [0.28, 0.72],
            k = 1
        )[0]

        sms_opt_in = random.choices(
            [True, False],
            weights = [0.13, 0.87],
            k = 1
        )[0]

        push_opt_in = random.choices(
            [True, False],
            weights = [0.61, 0.39],
            k = 1
        )[0]
    
    else:
        first_name = fake.first_name()
        last_name = fake.last_name()
        name = first_name + " " + last_name
        email = f'{first_name}.{last_name}@{fake.safe_domain_name()}'.lower()
        # Inconsistent gender label
        gender = random.choices(
            ["Female", "Male", "f", "m", "F", "M", ""],
            weights = [0.4, 0.4, 0.05, 0.03, 0.05, 0.1, 0.05],
            k=1
            )[0]
        # area, region = get_random_singapore_area_region()
        dob = fake.date_of_birth(minimum_age = 18, maximum_age = 85) if random.random() < 0.9 else None
        region, area = get_random_region_area()
        signup_date = fake.date_between(start_date='-6M', end_date='today') if random.random() < 0.95 else None
        loyalty_points = 0

        email_opt_in = random.choices(
            [True, False],
            weights = [0.28, 0.72],
            k = 1
        )[0]

        sms_opt_in = random.choices(
            [True, False],
            weights = [0.13, 0.87],
            k = 1
        )[0]

        push_opt_in = random.choices(
            [True, False],
            weights = [0.61, 0.39],
            k = 1
        )[0]
        

    # Wrong email format
    if customer_type != "Retail Walk-In":
        if random.random() < 0.05:
            if isinstance(email, str):
                email = email.replace('@','')

    customers.append({
        "customer_id": cid,
        "customer_type": customer_type,
        "name": name,
        "email": email,
        "gender": gender,
        "dob": dob,
        "area": area,
        "region": region,
        "signup_date": signup_date,
        "loyalty_points": loyalty_points,
        "email_marketing_opt_in": email_opt_in,
        "sms_opt_in": sms_opt_in,
        "push_notifications_opt_in": push_opt_in,
        "walk_in_flag": walk_in_flag
    })

i += 1

# Duplicates with minor variations
for _ in range(dirty_rows):
    original_cust = random.choice(customers)
    cust = original_cust.copy()
    cust["customer_id"] = f"CUST{i:03d}"
    if original_cust['email'] is not None:
        if isinstance(cust['email'], str):
            cust['email'] = cust['email'].replace('.', '_') if random.random() < 0.5 else cust['email']
            cust['email'] = cust['email'].replace('@','') if random.random() < 0.6 else cust['email']
            cust['email'] = cust['email'].replace('.com','') if random.random() < 0.2 else cust['email']
            cust['email'] = cust['email'].replace('example','exanple') if random.random() < 0.4 else cust['email']
            cust['email'] = cust['email'].replace('example','exampel') if random.random() < 0.1 else cust['email']
    if original_cust['dob'] is not None:
        cust["dob"] = fake.date_of_birth(minimum_age = 18, maximum_age = 85) if random.random() < 0.3 else cust['dob']
    customers.append(cust)
    i += 1

df_customers = pd.DataFrame(customers)
df_customers.to_csv("data_generation/raw_data/customers_raw.csv",index=False)
print("customers_raw.csv file generated")
