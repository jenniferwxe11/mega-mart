import json
import pandas as pd

# Downloaded file
file_path = 'data_generation/raw_data/singapore_areas.geojson'

try:
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract all region/area pairs
    region_area_pairs = []
    for feature in data["features"]:
        description = feature["properties"]["Description"]

        # Extract area and region from the Description string
        area = None
        region = None
        if "<th>PLN_AREA_N" in description:
            start = description.find("<td>", description.find("PLN_AREA_N")) + 4
            end = description.find("</td>", start)
            area = description[start:end].strip().title() 

        if "<th>REGION_N" in description:
            start = description.find("<td>", description.find("REGION_N")) + 4
            end = description.find("</td>", start)
            region = description[start:end].strip().replace(" REGION","").title()

        if area and region:
            region_area_pairs.append({
                "region": region,
                "area": area
            })

    df_region_areas = pd.DataFrame(region_area_pairs)
    df_region_areas.to_csv("data_generation/raw_data/region_areas.csv",index=False)
    print("region_areas.csv file generated")

except FileNotFoundError:
    print("File cannot be found")
