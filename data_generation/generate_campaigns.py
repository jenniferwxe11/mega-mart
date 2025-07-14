import random
import uuid
from datetime import timedelta

import pandas as pd
from dateutil.relativedelta import relativedelta
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CAMPAIGNS = 10

campaigns = []
campaign_ids = []

def generate_campaign_name():
    seasonal_phrases = [
        "Back to School", "Summer Savings", "Winter Deals", "Holiday Sale",
        "Mid-Year Mega Sale", "Black Friday", "End of Season", "Festive Sale",
        "New Year Kickoff", "Year-End Clearance", "Payday Deals", "Ramadan Specials"
    ]

    product_themes = [
        "Electronics Week", "Fresh Produce Fest", "Home Essentials Sale",
        "Gadget Galore", "Fashion Fever", "MegaMart Mart Madness"
    ]

    adjectives = ["Mega", "Hot", "Exclusive", "Limited-Time", "Weekly", "Flash", "VIP"]
    campaign_types = ["Sale", "Deals", "Discounts", "Event", "Campaign", "Promotions"]

    structure = random.choice(["seasonal", "product", "custom"])

    if structure == "seasonal":
        return f"MegaMart {random.choice(seasonal_phrases)}"
    elif structure == "product":
        return f"{random.choice(product_themes)}"
    else:
        return f"MegaMart {random.choice(adjectives)} {random.choice(campaign_types)}"

for _ in range(NUM_CAMPAIGNS):
    cid = str(uuid.uuid4())
    campaign_ids.append(cid)
    start = fake.date_between(start_date = '-6M', end_date = '-1M')
    if random.random() < 0.1:
        end = fake.date_between(start_date = '-6M', end_date = start)
    else:
        duration_type = random.choice(["1w", "2w", "1m"])
        
        if duration_type == "1w":
            end = start + timedelta(weeks=1)
        elif duration_type == "2w":
            end = start + timedelta(weeks=2)
        else:  # "1m"
            end = start + relativedelta(months=1)
    campaigns.append({
        "campaign_id": cid,
        "name": generate_campaign_name(),
        "channel": random.choice(["Email", "Push Notifications", "Social", "unknown"]),
        "budget": random.randint(1000,100000),
        "start_date": start,
        "end_date": end
    })

df_campaigns = pd.DataFrame(campaigns)
df_campaigns.to_csv("data_generation/raw_data/campaigns_raw.csv",index=False)
print("campaigns_raw.csv file generated")
