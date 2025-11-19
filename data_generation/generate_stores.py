import random

import pandas as pd
from config import NUM_PHYSICAL_STORES
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

stores = []
store_ids = []

region_area_df = pd.read_csv("data_generation/raw_data/region_areas.csv")

def get_random_region_area():
    row = region_area_df.sample(n=1).iloc[0]
    return row["region"], row["area"]

def get_region_from_area(area):
    row = region_area_df[region_area_df["area"] == area]
    if row.empty:
        print(f"Unknown {area}!")
    else:
        return row.iloc[0]["region"]

MALL_TO_AREA = { "Waterway Point": "Punggol", "Junction 8": "Bishan", "IMM": "Jurong East", "Northpoint": "Yishun", "Hougang Mall": "Hougang", "Causeway Point": "Woodlands", "NEX": "Serangoon", "VivoCity": "HarbourFront", "ION": "Orchard", "313@Somerset": "Somerset", "Bugis+": "Bugis", "The Seletar Mall": "Seletar", "Ang Mo Kio Hub": "Ang Mo Kio", "Sun Plaza": "Sembawang", "City Square Mall": "Farrer Park", "Westgate": "Jurong East", "JEM": "Jurong East", "Lot One": "Choa Chu Kang", "White Sands": "Pasir Ris", "Clarke Quay Central": "Clarke Quay", "Eastpoint Mall": "Pasir Ris", "Marina Square": "Marina Bay", "Raffles City": "Downtown Core", "Tampines Mall": "Tampines", "Great World City": "River Valley", "Plaza Singapura": "Dhoby Ghaut", "Orchard Central": "Orchard", "The Centrepoint": "Orchard", "Suntec City": "Marina Centre", "Funan Mall": "City Hall", "The Star Vista": "Buona Vista", "Bedok Mall": "Bedok", "Changi City Point": "Changi", "The Cathay": "Dhoby Ghaut", "Velocity": "Novena", "Kallang Wave Mall": "Kallang", "The Rail Mall": "Upper Bukit Timah", "The Clementi Mall": "Clementi", "Tanglin Mall": "Tanglin", "Millenia Walk": "Marina Bay", "West Coast Plaza": "West Coast", "Bukit Panjang Plaza": "Bukit Panjang", "Tiong Bahru Plaza": "Tiong Bahru", "Anchorpoint": "Alexandra", "The Woodleigh Mall": "Woodleigh", "Citylink Mall": "City Hall", "UE Square": "Bugis", "i12 Katong": "Marine Parade", "Marine Parade Central": "Marine Parade", "The Grandstand": "Bukit Timah", "Hillion Mall": "Bukit Panjang" }

for i in range(1, NUM_PHYSICAL_STORES + 1):
    sid = f"STOR{i:03d}"
    store_ids.append(sid)

    if random.random() < 0.8:
        mall = random.choice(list(MALL_TO_AREA.keys()))
        area = MALL_TO_AREA[mall]
        region = get_region_from_area(area)
        store_name = f"MegaMart {mall}"
        MALL_TO_AREA.pop(mall)

    else:
        block_no = random.randint(100, 999)
        region, area = get_random_region_area()
        store_name = f"MegaMart Blk {block_no} {area} Street"

    stores.append({
        "store_id": sid,
        "store_name": store_name,
        "area": area,
        "region": region,
        "store_type": "Physical Store"
    })

stores.append({
    "store_id": f"STOR{NUM_PHYSICAL_STORES+1:03d}",
    "store_name": "MegaMart Online",
    "area": "Nationwide",
    "region": "Nationwide",
    "store_type": "Online Website"
})

df_stores = pd.DataFrame(stores)
df_stores.to_csv("data_generation/raw_data/stores_raw.csv", index=False)
print("stores_raw.csv file generated")