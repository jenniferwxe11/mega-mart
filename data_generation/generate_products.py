import random

import pandas as pd
from config import NUM_PRODUCTS
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

products = []
product_ids = []
all_rows = []

MIN_REVIEWS = 5
MAX_REVIEWS = 20

CATEGORIES = [
    "Snacks", "Beverages", "Dairy & Eggs", "Frozen Food", "Fresh Produce",
    "Household Essentials", "Health & Beauty", "Baby Products", "Canned Goods",
    "Personal Care", "Meat & Seafood", "Bakery", "Cleaning Supplies", "Rice & Noodles",
    "Breakfast Foods"
]

BRANDS = {
    "Snacks": ["Lays", "Pringles", "Nature Valley", "KitKat", "Oreo"],
    "Beverages": ["Coca Cola", "Pepsi", "Nestle", "Lipton", "Minute Maid"],
    "Dairy & Eggs": ["Anchor", "Farmhouse", "Meadow Gold", "Marigold"],
    "Frozen Food": ["Birds Eye", "Green Giant", "McCain"],
    "Fresh Produce": ["Dole", "Chiquita", "Local Farms"],
    "Household Essentials": ["Dettol", "Clorox", "Finish", "3M"],
    "Health & Beauty": ["Nivea", "Colgate", "Dove", "L'Oreal"],
    "Baby Products": ["Pampers", "Huggies", "Johnson's Baby"],
    "Canned Goods": ["Del Monte", "Heinz", "Campbell's"],
    "Personal Care": ["Pantene", "Head & Shoulders", "Gillette"],
    "Meat & Seafood": ["Farmhouse", "OceanFresh", "Sea Best"],
    "Bakery": ["Gardenia", "Bimbo", "Wonder Bread"],
    "Cleaning Supplies": ["Ajax", "Mr Muscle", "Vanish"],
    "Rice & Noodles": ["Tilda", "MamyPoko", "Maggi"],
    "Breakfast Foods": ["Kellogg's", "Quaker", "Post"]
}

CATEGORY_ITEMS = {
    "Snacks": ["Chips", "Biscuits", "Bars", "Cookies", "Nuts"],
    "Beverages": ["Cola", "Juice", "Tea", "Coffee", "Soda"],
    "Dairy & Eggs": ["Milk", "Cheese", "Butter", "Yogurt", "Cream"],
    "Frozen Food": ["Peas", "Pizza", "Fries", "Fish Fingers", "Dumplings"],
    "Fresh Produce": ["Apples", "Bananas", "Carrots", "Tomatoes", "Spinach"],
    "Household Essentials": ["Detergent", "Soap", "Cleaner", "Spray", "Wipes"],
    "Health & Beauty": ["Lotion", "Shampoo", "Toothpaste", "Soap", "Conditioner"],
    "Baby Products": ["Diapers", "Wipes", "Powder", "Cream", "Formula"],
    "Canned Goods": ["Tomatoes", "Corn", "Beans", "Tuna", "Soup"],
    "Personal Care": ["Shampoo", "Conditioner", "Soap", "Deodorant", "Gel"],
    "Meat & Seafood": ["Chicken", "Beef", "Fish", "Prawns", "Bacon"],
    "Bakery": ["Bread", "Cake", "Buns", "Croissant", "Muffin"],
    "Cleaning Supplies": ["Detergent", "Bleach", "Spray", "Scrub", "Wipes"],
    "Rice & Noodles": ["Rice", "Pasta", "Noodles", "Vermicelli", "Spaghetti"],
    "Breakfast Foods": ["Cereal", "Oats", "Granola", "Muesli", "Porridge"]
}

CATEGORY_DESCRIPTORS = {
    "Snacks": {
        "taste": ["salty", "savory", "spicy", "sweet", "umami", "tangy"],
        "texture": ["crunchy", "crispy", "soft", "chewy", "firm", "flaky"]
    },
    "Beverages": {
        "taste": ["sweet", "bitter", "refreshing", "sour", "fruity", "carbonated"],
        "texture": ["smooth", "frothy", "watery", "creamy", "thick", "light"]
    },
    "Dairy & Eggs": {
        "taste": ["creamy", "milky", "rich", "bland", "fresh", "tangy"],
        "texture": ["soft", "smooth", "runny", "firm", "dense", "fluffy"]
    },
    "Frozen Food": {
        "taste": ["savory", "bland", "spicy", "rich"],
        "texture": ["soft", "crispy", "chewy", "frozen", "flaky"]
    },
    "Fresh Produce": {
        "taste": ["fresh", "sweet", "bitter", "tangy", "juicy", "earthy"],
        "texture": ["crisp", "firm", "soft", "juicy", "fibrous"]
    },
    "Household Essentials": {
        "texture": ["smooth", "abrasive", "soft", "durable"],
        "packaging": ["easy to open", "leak-proof", "compact", "bulk"]
    },
    "Health & Beauty": {
        "texture": ["smooth", "silky", "creamy", "moisturizing", "light"],
        "scent": ["floral", "fresh", "fruity", "herbal", "unscented"]
    },
    "Baby Products": {
        "texture": ["soft", "gentle", "absorbent", "smooth"],
        "scent": ["mild", "unscented", "fresh", "soothing"]
    },
    "Canned Goods": {
        "taste": ["savory", "bland", "spicy", "sweet"],
        "texture": ["soft", "firm", "chunky", "smooth"]
    },
    "Personal Care": {
        "texture": ["smooth", "creamy", "gentle", "soft", "moisturizing"],
        "scent": ["floral", "fresh", "fruity", "unscented", "soothing"]
    },
    "Meat & Seafood": {
        "taste": ["savory", "umami", "rich", "fresh", "slightly sweet"],
        "texture": ["tender", "firm", "juicy", "flaky", "chewy"]
    },
    "Bakery": {
        "taste": ["buttery", "sweet", "savory", "flavorful", "rich", "fresh"],
        "texture": ["soft", "fluffy", "crispy", "crumbly", "chewy"]
    },
    "Cleaning Supplies": {
        "texture": ["smooth", "abrasive", "soft", "foamy"],
        "scent": ["fresh", "citrusy", "unscented", "clean"]
    },
    "Rice & Noodles": {
        "taste": ["bland", "savory", "nutty", "umami", "slightly sweet"],
        "texture": ["soft", "firm", "chewy", "al dente", "fluffy"]
    },
    "Breakfast Foods": {
        "taste": ["sweet", "savory", "nutty", "fruity", "rich"],
        "texture": ["crispy", "soft", "fluffy", "smooth", "chewy"]
    }
}

STATUS = ["active", "discontinued", "promotion"]

positive_adjectives = [
    "excellent", "amazing", "great", "fantastic", "high-quality", "perfect",
    "superb", "wonderful", "impressive", "top-notch", "outstanding"
]

negative_adjectives = [
    "disappointing", "poor", "terrible", "low-quality", "bad", "unsatisfactory",
    "inferior", "flawed", "subpar", "mediocre", "unpleasant"
]

neutral_phrases = [
    "average", "okay", "fine", "nothing special", "acceptable",
    "decent", "passable", "satisfactory", "moderate", "so-so"
]

positive_verbs = [
    "love", "enjoyed", "liked", "appreciated", "recommend",
    "adore", "favor", "admire", "cherish", "value"
]

negative_verbs = [
    "disliked", "regret buying", "was unhappy with", "would not buy again", "complain about",
    "detest", "cannot recommend", "feel let down by", "avoid", "beware of"
]

neutral_verbs = ["found", "tried", "tested", "used", "experienced"]
mention_types = ["none", "name", "price", "taste", "texture", "packaging", "promotion"]

def generate_review(product_name, category, price):
    sentiment = random.choices(["positive","neutral","negative"], weights=[0.6,0.2,0.2])[0]

    taste_options = CATEGORY_DESCRIPTORS.get(category, {}).get("taste", [])
    texture_options = CATEGORY_DESCRIPTORS.get(category, {}).get("texture", [])
    scent_options = CATEGORY_DESCRIPTORS.get(category, {}).get("scent", [])
    taste = random.choice(taste_options) if taste_options else None
    texture = random.choice(texture_options) if texture_options else None
    scent = random.choice(scent_options) if scent_options else None
    packaging = random.choice(["loosely packaged", "damaged", "well-packaged"]) if random.random() < 0.3 else None
    promotion = random.choice(["good deal", "buy 1 get 1", "limited offer"]) if random.random() < 0.2 else None

    mention_weights = [0.4, 0.25, 0.1, 0.1, 0.05, 0.05, 0.05]
    mention_type = random.choices(mention_types, weights=mention_weights, k=1)[0]
    mention_text = ""
    if mention_type == "price" and price is not None:
        mention_text = f" At ${price}, I think it's worth considering."
    elif mention_type == "taste" and taste is not None:
        mention_text = random.choice([
            f" The taste is quite {taste}.",
            f" I really noticed the {taste} flavor of {product_name}.",
            f" Tastes {taste}, just as expected."
        ])
    elif mention_type == "texture" and texture is not None:
        mention_text = random.choice([
            f" The texture is {texture}.",
            f" I found {product_name} {texture} when using it.",
            f" Feels {texture} and pleasant to use."
        ])
    elif mention_type == "scent" and scent is not None:
        mention_text = random.choice([
            f" {product_name} smells {scent}.",
            f" The {scent} scent is noticeable.",
            f" Has a {scent} aroma that I liked."
        ])
    elif mention_type == "packaging" and packaging is not None:
        mention_text = random.choice([
            f" The packaging was {packaging}.",
            f" I liked how the item was {packaging}.",
            f" Packaged {packaging}, very convenient."
        ])
    elif mention_type == "promotion" and promotion is not None:
        mention_text = random.choice([
            f" I got it during a {promotion}, which was nice.",
            f" Took advantage of the {product_name} {promotion} deal.",
            f" Purchased it with a {promotion} offer."
        ])
    
    positive_templates = [
        f"{random.choice(positive_verbs).capitalize()} this product! It's {random.choice(positive_adjectives)}.{mention_text}",
        f"This product is {random.choice(positive_adjectives)} and I {random.choice(positive_verbs)} it.{mention_text}",
        f"Absolutely {random.choice(positive_adjectives)}! {random.choice(positive_verbs).capitalize()} it.{mention_text}",
        f"I {random.choice(positive_verbs)} {product_name}. Truly {random.choice(positive_adjectives)}.{mention_text}",
        f"{product_name} exceeded my expectations. {random.choice(positive_verbs).capitalize()} it!{mention_text}",
        f"I've been using {product_name} for a while and it's {random.choice(positive_adjectives)}.{mention_text}",
        f"{random.choice(positive_verbs).capitalize()} this! {product_name} is {random.choice(positive_adjectives)}.",
        f"Highly {random.choice(['recommended', 'suggested', 'endorsed'])}! {product_name} is {random.choice(positive_adjectives)}.{mention_text}",
        f"Can't get enough of {product_name}! It's {random.choice(positive_adjectives)}.{mention_text}",
        f"One of the best purchases I've made this year! {product_name} is {random.choice(positive_adjectives)}.{mention_text}",
        f"{product_name} really impressed me. {random.choice(positive_verbs).capitalize()} it!{mention_text}"
    ]

    neutral_templates = [
        f"This product is {random.choice(neutral_phrases)}.{mention_text}",
        f"I found {product_name} to be {random.choice(neutral_phrases)}.{mention_text}",
        f"{product_name} is {random.choice(neutral_phrases)}, nothing fancy.{mention_text}",
        f"Overall, {product_name} seems {random.choice(neutral_phrases)}.{mention_text}",
        f"{product_name} is okay. {random.choice(['Nothing special', 'Meets expectations', 'Average quality'])}.{mention_text}",
        f"Using {product_name} was {random.choice(neutral_phrases)}. Would buy again? Not sure.{mention_text}",
        f"Just tried {product_name}. It's {random.choice(neutral_phrases)}.{mention_text}",
        f"{product_name} serves its purpose. {random.choice(neutral_phrases).capitalize()} quality.{mention_text}",
        f"Nothing extraordinary about {product_name}. It's {random.choice(neutral_phrases)}.{mention_text}",
        f"{product_name} is acceptable for the price.{mention_text}"
    ]

    negative_templates = [
        f"{random.choice(negative_verbs).capitalize()} {product_name}. It's {random.choice(negative_adjectives)}.{mention_text}",
        f"I {random.choice(negative_verbs)} this product. {product_name} felt {random.choice(negative_adjectives)}.{mention_text}",
        f"Unfortunately, {product_name} is {random.choice(negative_adjectives)}. {random.choice(negative_verbs).capitalize()} it.{mention_text}",
        f"{product_name} did not meet my expectations. {random.choice(negative_verbs).capitalize()} it.{mention_text}",
        f"Really {random.choice(negative_adjectives)} experience with {product_name}.{mention_text}",
        f"{product_name} disappointed me. {random.choice(negative_verbs).capitalize()} it!{mention_text}",
        f"Not impressed with {product_name}. It's {random.choice(negative_adjectives)}.{mention_text}",
        f"{product_name} didn't live up to the hype. {random.choice(negative_verbs).capitalize()} this product.{mention_text}",
        f"{random.choice(negative_adjectives).capitalize()} quality. I {random.choice(negative_verbs)} {product_name}.{mention_text}",
        f"{product_name} is subpar. {random.choice(negative_verbs).capitalize()} it.{mention_text}",
        f"Very {random.choice(negative_adjectives)}! {product_name} is disappointing.{mention_text}"
    ]

    if sentiment == "positive":
        text = random.choice(positive_templates)
        stars = random.randint(4,5)
    elif sentiment == "neutral":
        text = random.choice(neutral_templates)
        stars = 3
    else:
        text = random.choice(negative_templates)
        stars = random.randint(1,2)

    texting_shorthand = {
        "you": "u",
        "are": "r",
        "please": "pls",
        "people": "ppl",
        "message": "msg",
        "before": "b4",
        "with": "w",
        "really": "rly",
        "thanks": "thx",
        "okay": "ok",
        "see": "c",
        "about": "abt",
        "today": "tdy",
        "very": "v",
        "great": "gr8",
        "love": "luv"
    }

    if random.random() < 0.25:
        for word, short in texting_shorthand.items():
            if random.random() < 0.5:
                text = text.replace(word, short)

    if random.random() < 0.3:
        text = text.lower()

    review = {
        "username": fake.user_name(),
        "stars": stars,
        "review_text": text,
        "review_date": fake.date_between(start_date="-6M", end_date="today").isoformat()
    }

    return review

for i in range(1, NUM_PRODUCTS + 1):
    pid = f"PROD{i:03d}"
    product_ids.append(pid)

    category = random.choice(CATEGORIES)
    brand = random.choice(BRANDS.get(category, ["Generic"]))
    item = random.choice(CATEGORY_ITEMS.get(category, ["Item"]))
    
    # product name with intentional casing errors
    name = f"{random.choice(['Premium', 'Classic', 'Deluxe', 'Extra'])} {brand} {item}"
    if random.random() < 0.05:
        name = name.upper()
    
    # category typos
    category_name = category
    if random.random() < 0.03:
        category_name = category_name.replace("a", "@").replace("o","0")
    
    # Prices
    selling_price = round(random.uniform(1.5, 100), 2)
    cost_price = round(selling_price * random.uniform(0.5, 0.95), 2)
    
    status = random.choices(STATUS, weights=[0.85,0.05,0.10])[0]
    
    # Stock labels (with inconsistencies)
    stock = random.choices(
        ["in stock", "instock", "OUT OF STOCK", None],
        weights=[0.7, 0.1, 0.15, 0.05]
    )[0]
    
    # Introduce missing price randomly
    if random.random() < 0.05:
        selling_price = None
    
    review_count = random.randint(MIN_REVIEWS, MAX_REVIEWS)
    reviews = [generate_review(name, category_name, selling_price) for _ in range(review_count)]
    
    for review in reviews:
        all_rows.append({
            "product_id": pid,
            "name": name,
            "brand": brand,
            "category": category_name,
            "selling_price": selling_price,
            "cost_price": cost_price,
            "status": status,
            "stock": stock,
            "username": review["username"],
            "stars": review["stars"],
            "review_text": review["review_text"],
            "review_date": review["review_date"]
        })

df = pd.DataFrame(all_rows)
df.to_csv("data_generation/raw_data/products_raw.csv", index=False)
print("products_raw.csv file generated")
