import random

from datetime import timedelta
import string
import pandas as pd
from config import NUM_CAMPAIGNS
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

campaigns = []
campaign_ids = []

def generate_campaign_name():

    adjectives = ["Mega", "Hot", "Exclusive", "Limited-Time", "Weekly", "Flash", "VIP"]
    campaign_types = ["Sale", "Deals", "Offer", "Event", "Promotions"]
    return f"MegaMart {random.choice(adjectives)} {random.choice(campaign_types)}"

def generate_discount_code():
    prefix = random.choice(["SAVE", "DEAL", "MEGA", "PROMO"])
    number = random.randint(5, 50)
    suffix = ''.join(random.choices(string.ascii_uppercase, k=2))
    return f"{prefix}{number}{suffix}"

for i in range(1, NUM_CAMPAIGNS + 1):
    cid = f"CAMP{i:03d}"
    campaign_ids.append(cid)
    start = fake.date_between(start_date = '-6M', end_date = '-1M')
    end = start + timedelta(weeks=1)
    budget = int(round(random.randint(500,50000)/100))*100
    base = min(budget/50000, 1.0)
    offer_type = random.choice(["Discount", "Free-Shipping"])
    if offer_type == "Discount":
        discount_percentage = random.randint(5,30)
        discount_code = generate_discount_code()
        free_shipping = False
    elif offer_type == "Free-Shipping":
        discount_percentage = None
        discount_code = None
        free_shipping = True
    is_ab_test = random.random() < 0.3
    campaigns.append({
        "campaign_id": cid,
        "name": generate_campaign_name(),
        "channel": random.choice(["Email", "Push Notifications", "SMS"]),
        "budget": f"${budget}",
        "start_date": start,
        "end_date": end,
        "offer_type": offer_type,
        "discount_percentage": discount_percentage,
        "discount_code": discount_code,
        "free_shipping": free_shipping,
        "is_ab_test": is_ab_test,
        "kpi_conversion_uplift_target": round(0.02 + base * random.uniform(0.03, 0.15), 3),
        "kpi_revenue_uplift_target": round(0.03 + base * random.uniform(0.05, 0.25), 3),
        "kpi_engagement_target": round(0.05 + base * random.uniform(0.10, 0.35), 3),
    })

df_campaigns = pd.DataFrame(campaigns)
df_campaigns.to_csv("data_generation/raw_data/campaigns_raw.csv",index=False)
print("campaigns_raw.csv file generated")
