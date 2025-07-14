import random
import uuid
from datetime import timedelta

import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CLICKSTREAMS = 2000

clickstreams = []
clickstream_ids = []

customers_df = pd.read_csv("data_generation/raw_data/customers_raw.csv")
customer_ids = customers_df["customer_id"].dropna().tolist()

campaigns_df = pd.read_csv("data_generation/raw_data/campaigns_raw.csv")
campaign_ids = campaigns_df["campaign_id"].dropna().tolist()

event_types = ["view",
            "click",
            "add_to_cart",
            "remove_from_cart",
            "scroll",
            "search",
            "checkout_start",
            "payment_success",
            "",
            None,
            "invalid_event"]

categories = ["groceries",
            "electronics",
            "fashion",
            "home",
            "toys"]

referrers = [
    "google.com", "facebook.com", "instagram.com", "tiktok.com", "shopee.sg",
    "lazada.sg", "grab.com", "mothership.sg", "youtube.com", "straitstimes.com",
    "telegram.org", "gov.sg", "", None
]

locations = [
    "Singapore", "Kuala Lumpur", "Jakarta", "Bangkok", "Manila", "Ho Chi Minh City",
    "Hong Kong", "Taipei", "Shanghai", "Beijing", "Tokyo", "Seoul",
    "New York", "London", "Sydney", "Melbourne", "Los Angeles", "San Francisco",
    "Dubai", "Mumbai", "Delhi"
]

search_terms = [
    "milo", "air fryer", "xiaomi phone", "neck fan", "foldable table", "instant noodles",
    "power bank", "running shoes", "mooncake", "humidifier", "blackpink album",
    "crocs", "school bag", "rice cooker", "kdrama merch", "nasi lemak", "durian"
]

for _ in range(NUM_CLICKSTREAMS):
    session_id = str(uuid.uuid4())
    customer_id = random.choice(customer_ids + [None,""])
    campaign_id = random.choice(campaign_ids + [None,""])
    event_count = random.randint(1,5)
    session_time = fake.date_time_between(start_date = '-30d', end_date = 'now')
    # correspond logic with the campaign time and transaction time etc

    for event_index in range(event_count):
        clickstream_id = f"{session_id}_{event_index}"
        clickstream_ids.append(clickstream_id)

        timestamp = session_time + timedelta(seconds = random.randint(1,300))
        if random.random() < 0.01:
            timestamp = None

        event_type = random.choices(
            event_types,
            weights = [35, 25, 15, 3, 10, 6, 4, 1, 0.5, 0.3, 0.2],
            k=1
        )[0]

        search_term = random.choice(search_terms)

        page = random.choice([
                "/home",
                f"/product/{fake.random_int(min=1,max=1000)}",
                f"/category/{random.choice(categories)}"
                "/cart",
                "/checkout",
                f"/search?q={search_term.replace(' ','+')}"
            ])
        
        device_type = random.choice(["Mobile", "Desktop", "Tablet"])
        referrer = random.choice(referrers)
        location = random.choice(locations)

        clickstreams.append({
            "clickstream_id": clickstream_id,
            "session_id": session_id,
            "customer_id": customer_id,
            "campaign_id": campaign_id,
            "timestamp": timestamp,
            "event_type": event_type,
            "page": page,
            "device_type": device_type,
            "referrer": referrer,
            "location": location
        })
    

df_clickstreams = pd.DataFrame(clickstreams)
df_clickstreams.to_csv("data_generation/raw_data/clickstreams_raw.csv",index=False)
print("clickstreams_raw.csv file generated")
    