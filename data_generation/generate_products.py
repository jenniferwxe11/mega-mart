import random
from typing import Optional

import pandas as pd
from config import MAX_REVIEWS, MIN_REVIEWS, NUM_PRODUCTS
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

CATEGORIES = [
    "Snacks",
    "Beverages",
    "Dairy & Eggs",
    "Frozen Food",
    "Fresh Produce",
    "Household Essentials",
    "Health & Beauty",
    "Baby Products",
    "Canned Goods",
    "Personal Care",
    "Meat & Seafood",
    "Bakery",
    "Cleaning Supplies",
    "Rice & Noodles",
    "Breakfast Foods",
    "Electronics & Applicances",
    "Home & Living (Kitchenware, Storage, Bedding)",
    "Lifestyle & Recreation (Fitness, Toys, Travel)",
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
    "Breakfast Foods": ["Kellogg's", "Quaker", "Post"],
    "Electronics & Applicances": ["Philips", "Samsung", "Xiaomi", "Dyson", "Panasonic"],
    "Home & Living (Kitchenware, Storage, Bedding)": [
        "IKEA",
        "Tefal",
        "Lock&Lock",
        "Zojirushi",
        "HomeBasics",
    ],
    "Lifestyle & Recreation (Fitness, Toys, Travel)": [
        "Nike",
        "Adidas",
        "Decathlon",
        "LEGO",
        "Samsonite",
    ],
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
    "Breakfast Foods": ["Cereal", "Oats", "Granola", "Muesli", "Porridge"],
    "Electronics & Applicances": [
        "Headphones",
        "Blender",
        "Air Fryer",
        "Smartwatch",
        "Vacuum Cleaner",
    ],
    "Home & Living (Kitchenware, Storage, Bedding)": [
        "Cookware",
        "Food Containers",
        "Bedsheets",
        "Pillows",
        "Storage Boxes",
    ],
    "Lifestyle & Recreation (Fitness, Toys, Travel)": [
        "Dumbbells",
        "Yoga Mat",
        "Board Games",
        "Suitcase",
        "Sports Bottle",
    ],
}

GLOBAL_DESCRIPTORS = {
    "packaging": {
        "positive": ["well-packaged", "securely packaged", "neatly packed"],
        "neutral": ["standard packaging", "average packaging"],
        "negative": ["loosely packaged", "damaged", "flimsy packaging"],
    },
    "promotion": {
        "positive": ["good deal", "limited offer", "buy 1 get 1"],
        "neutral": ["standard offer", "price as usual"],
        "negative": ["expensive for value", "poor deal", "not worth the promotion"],
    },
}

POSITIVE_CATEGORY_DESCRIPTORS = {
    "Snacks": {
        "taste": ["salty", "savory", "spicy", "sweet", "umami", "tangy"],
        "texture": ["crunchy", "crispy", "soft", "chewy", "firm", "flaky"],
    },
    "Beverages": {
        "taste": ["sweet", "bitter", "refreshing", "sour", "fruity", "carbonated"],
        "texture": ["smooth", "frothy", "watery", "creamy", "thick", "light"],
    },
    "Dairy & Eggs": {
        "taste": ["creamy", "milky", "rich", "bland", "fresh", "tangy"],
        "texture": ["soft", "smooth", "runny", "firm", "dense", "fluffy"],
    },
    "Frozen Food": {
        "taste": ["savory", "bland", "spicy", "rich"],
        "texture": ["soft", "crispy", "chewy", "frozen", "flaky"],
    },
    "Fresh Produce": {
        "taste": ["fresh", "sweet", "bitter", "tangy", "juicy", "earthy"],
        "texture": ["crisp", "firm", "soft", "juicy", "fibrous"],
    },
    "Household Essentials": {
        "texture": ["smooth", "abrasive", "soft", "durable"],
        "packaging": ["easy to open", "leak-proof", "compact", "bulk"],
    },
    "Health & Beauty": {
        "texture": ["smooth", "silky", "creamy", "moisturizing", "light"],
        "scent": ["floral", "fresh", "fruity", "herbal", "unscented"],
    },
    "Baby Products": {
        "texture": ["soft", "gentle", "absorbent", "smooth"],
        "scent": ["mild", "unscented", "fresh", "soothing"],
    },
    "Canned Goods": {
        "taste": ["savory", "bland", "spicy", "sweet"],
        "texture": ["soft", "firm", "chunky", "smooth"],
    },
    "Personal Care": {
        "texture": ["smooth", "creamy", "gentle", "soft", "moisturizing"],
        "scent": ["floral", "fresh", "fruity", "unscented", "soothing"],
    },
    "Meat & Seafood": {
        "taste": ["savory", "umami", "rich", "fresh", "slightly sweet"],
        "texture": ["tender", "firm", "juicy", "flaky", "chewy"],
    },
    "Bakery": {
        "taste": ["buttery", "sweet", "savory", "flavorful", "rich", "fresh"],
        "texture": ["soft", "fluffy", "crispy", "crumbly", "chewy"],
    },
    "Cleaning Supplies": {
        "texture": ["smooth", "abrasive", "soft", "foamy"],
        "scent": ["fresh", "citrusy", "unscented", "clean"],
    },
    "Rice & Noodles": {
        "taste": ["bland", "savory", "nutty", "umami", "slightly sweet"],
        "texture": ["soft", "firm", "chewy", "al dente", "fluffy"],
    },
    "Breakfast Foods": {
        "taste": ["sweet", "savory", "nutty", "fruity", "rich"],
        "texture": ["crispy", "soft", "fluffy", "smooth", "chewy"],
    },
    "Electronics & Applicances": {
        "performance": ["fast", "efficient", "powerful", "responsive", "smooth"],
        "build": ["durable", "sturdy", "lightweight", "compact", "well-built"],
        "usage": ["easy to use", "user-friendly", "intuitive", "versatile"],
    },
    "Home & Living (Kitchenware, Storage, Bedding)": {
        "material": ["sturdy", "lightweight", "soft", "premium", "durable"],
        "comfort": ["comfortable", "supportive", "cozy", "soft-touch"],
        "design": ["minimalist", "modern", "practical", "space-saving"],
    },
    "Lifestyle & Recreation (Fitness, Toys, Travel)": {
        "experience": ["engaging", "fun", "effective", "challenging", "enjoyable"],
        "durability": ["sturdy", "long-lasting", "high-quality", "robust"],
        "convenience": ["portable", "easy to carry", "lightweight", "travel-friendly"],
    },
}


NEUTRAL_CATEGORY_DESCRIPTORS = {
    "Snacks": {
        "taste": ["moderate", "balanced", "ordinary", "mild", "typical"],
        "texture": ["soft", "slightly crunchy", "standard", "average", "acceptable"],
    },
    "Beverages": {
        "taste": ["average", "mild", "slightly sweet", "standard", "typical"],
        "texture": ["light", "smooth", "watery", "average", "ordinary"],
    },
    "Dairy & Eggs": {
        "taste": ["mild", "plain", "average", "acceptable", "typical"],
        "texture": ["soft", "standard", "slightly firm", "average", "acceptable"],
    },
    "Frozen Food": {
        "taste": ["bland", "typical", "standard", "moderate"],
        "texture": ["soft", "slightly crispy", "acceptable", "frozen-like", "ordinary"],
    },
    "Fresh Produce": {
        "taste": ["average", "fresh enough", "ordinary", "mild", "typical"],
        "texture": ["firm enough", "soft", "average", "acceptable", "slightly crisp"],
    },
    "Household Essentials": {
        "texture": ["standard", "soft", "average", "durable enough"],
        "packaging": ["normal packaging", "typical", "average"],
    },
    "Health & Beauty": {
        "texture": ["average", "smooth enough", "light", "acceptable"],
        "scent": ["mild", "barely noticeable", "neutral", "ordinary"],
    },
    "Baby Products": {
        "texture": ["soft enough", "acceptable", "average", "standard"],
        "scent": ["neutral", "unscented", "mild", "ordinary"],
    },
    "Canned Goods": {
        "taste": ["average", "typical", "plain", "standard"],
        "texture": ["soft enough", "average", "acceptable", "standard"],
    },
    "Personal Care": {
        "texture": ["average", "standard", "soft", "acceptable"],
        "scent": ["neutral", "mild", "barely noticeable", "ordinary"],
    },
    "Meat & Seafood": {
        "taste": ["ordinary", "mild", "standard", "average"],
        "texture": ["acceptable", "average", "firm enough", "typical"],
    },
    "Bakery": {
        "taste": ["average", "standard", "mildly sweet", "typical"],
        "texture": ["soft", "standard", "slightly fluffy", "acceptable"],
    },
    "Cleaning Supplies": {
        "texture": ["average", "standard", "smooth enough", "acceptable"],
        "scent": ["mild", "neutral", "barely noticeable", "ordinary"],
    },
    "Rice & Noodles": {
        "taste": ["average", "plain", "acceptable", "standard"],
        "texture": ["soft enough", "average", "typical", "al dente-ish"],
    },
    "Breakfast Foods": {
        "taste": ["standard", "mild", "average", "typical"],
        "texture": ["soft", "average", "acceptable", "ordinary"],
    },
    "Electronics & Applicances": {
        "performance": ["adequate", "acceptable", "standard", "satisfactory"],
        "build": ["average", "standard", "acceptable", "adequate"],
        "usage": ["functional", "okay", "average", "acceptable"],
    },
    "Home & Living (Kitchenware, Storage, Bedding)": {
        "material": ["standard", "average", "acceptable", "functional"],
        "comfort": ["moderate", "acceptable", "okay", "standard"],
        "design": ["plain", "average", "standard", "functional"],
    },
    "Lifestyle & Recreation (Fitness, Toys, Travel)": {
        "experience": ["okay", "average", "moderate", "standard"],
        "durability": ["adequate", "average", "standard", "acceptable"],
        "convenience": ["acceptable", "average", "standard", "okay"],
    },
}

NEGATIVE_CATEGORY_DESCRIPTORS = {
    "Snacks": {
        "taste": ["bland", "stale", "overly salty", "too sweet", "artificial", "off"],
        "texture": [
            "soggy",
            "stale",
            "hard",
            "chewy in a bad way",
            "crumbly",
            "greasy",
        ],
    },
    "Beverages": {
        "taste": ["bitter", "watery", "flat", "too sweet", "off", "unpleasant"],
        "texture": ["thin", "watery", "foamy in a bad way", "chalky", "gritty"],
    },
    "Dairy & Eggs": {
        "taste": ["bland", "sour", "rancid", "stale", "flat", "off"],
        "texture": [
            "runny",
            "clumpy",
            "watery",
            "gritty",
            "rubbery",
            "dense in a bad way",
        ],
    },
    "Frozen Food": {
        "taste": ["bland", "frozen-tasting", "salty", "stale", "off", "oily"],
        "texture": ["frozen-hard", "chewy in a bad way", "mushy", "stale", "rubbery"],
    },
    "Fresh Produce": {
        "taste": ["bitter", "sour", "mealy", "watery", "off", "bland"],
        "texture": ["wilted", "soft in a bad way", "fibrous", "mushy", "dry"],
    },
    "Household Essentials": {
        "texture": ["rough", "flimsy", "cheap", "scratches easily", "fragile"],
        "packaging": ["hard to open", "leaky", "damaged", "bulk in a bad way"],
    },
    "Health & Beauty": {
        "texture": ["greasy", "sticky", "runny", "thin", "unpleasant"],
        "scent": [
            "strong in a bad way",
            "chemical",
            "artificial",
            "off-putting",
            "unpleasant",
        ],
    },
    "Baby Products": {
        "texture": ["rough", "scratchy", "absorbent in a bad way", "cheap"],
        "scent": ["strong", "chemical", "off", "unpleasant"],
    },
    "Canned Goods": {
        "taste": ["bland", "sour", "metallic", "too salty", "off"],
        "texture": ["mushy", "too soft", "chunky in a bad way", "watery"],
    },
    "Personal Care": {
        "texture": ["greasy", "thin", "sticky", "watery", "unpleasant"],
        "scent": ["overpowering", "chemical", "strong", "unpleasant"],
    },
    "Meat & Seafood": {
        "taste": ["gamey", "bland", "sour", "overcooked", "off"],
        "texture": ["tough", "dry", "rubbery", "chewy in a bad way", "stringy"],
    },
    "Bakery": {
        "taste": ["stale", "bland", "too sweet", "dry", "off", "flat"],
        "texture": [
            "dry",
            "crumbly in a bad way",
            "hard",
            "dense",
            "chewy in a bad way",
        ],
    },
    "Cleaning Supplies": {
        "texture": ["harsh", "abrasive", "slimy", "chemical", "rough"],
        "scent": ["overpowering", "chemical", "strong", "unpleasant"],
    },
    "Rice & Noodles": {
        "taste": ["bland", "starchy", "underseasoned", "overcooked", "off"],
        "texture": ["mushy", "sticky", "too firm", "dry", "clumpy"],
    },
    "Breakfast Foods": {
        "taste": ["bland", "overly sweet", "stale", "off", "mediocre"],
        "texture": ["soggy", "dense", "rubbery", "dry", "chewy in a bad way"],
    },
    "Electronics & Applicances": {
        "performance": ["slow", "laggy", "unresponsive", "inefficient", "fragile"],
        "build": ["flimsy", "cheap", "brittle", "unstable", "fragile"],
        "usage": ["complicated", "confusing", "frustrating", "inconvenient"],
    },
    "Home & Living (Kitchenware, Storage, Bedding)": {
        "material": ["cheap", "flimsy", "rough", "low-quality", "fragile"],
        "comfort": ["uncomfortable", "unsupportive", "hard", "scratchy", "rough"],
        "design": ["awkward", "unattractive", "clunky", "impractical", "bulky"],
    },
    "Lifestyle & Recreation (Fitness, Toys, Travel)": {
        "experience": [
            "boring",
            "frustrating",
            "difficult",
            "underwhelming",
            "disappointing",
        ],
        "durability": [
            "fragile",
            "short-lived",
            "poor quality",
            "breaks easily",
            "flimsy",
        ],
        "convenience": [
            "cumbersome",
            "heavy",
            "inconvenient",
            "awkward to carry",
            "unportable",
        ],
    },
}

POSITIVE_DESCRIPTOR_TEMPLATES = {
    "price": [
        "At ${value}, I think it's worth considering.",
        "Price-wise, ${value} seems fair for what you get.",
        "For ${value}, this is a good deal.",
        "Considering the quality, ${value} is reasonable.",
        "${value} feels like a worthwhile investment.",
        "The cost of ${value} is justified by its performance.",
    ],
    "taste": [
        "The taste is quite ${value}.",
        "I really noticed the ${value} flavor of ${product}.",
        "Tastes ${value}, just as expected.",
        "${product} has a ${value} flavor that's enjoyable.",
        "Really loved the ${value} taste in this one.",
        "The ${value} flavor is prominent and appealing.",
        "I found the taste to be pleasantly ${value}.",
        "${product} delivers a ${value} flavor experience.",
    ],
    "texture": [
        "The texture is ${value}.",
        "I found ${product} ${value} when using it.",
        "Feels ${value} and pleasant to use.",
        "Has a ${value} consistency that feels nice.",
        "The ${value} texture really stands out.",
        "Texture is ${value}, which I enjoyed.",
        "Really ${value} texture overall.",
    ],
    "scent": [
        "${product} smells ${value}.",
        "The ${value} scent is noticeable.",
        "Has a ${value} aroma that I liked.",
        "The ${value} fragrance adds to the overall experience.",
        "A subtle ${value} scent is present and pleasant.",
        "${product} gives off a ${value} smell that's enjoyable.",
        "The ${value} aroma is appealing and refreshing.",
        "Really appreciated the ${value} scent in this product.",
    ],
    "performance": [
        "Performance-wise, it's very ${value}.",
        "It performs ${value} for its category.",
        "Really impressed by how ${value} it is.",
        "The ${product} is ${value} in operation.",
        "Handles tasks in a ${value} manner.",
    ],
    "build": [
        "The build quality feels ${value}.",
        "Feels ${value} and solid in hand.",
        "Really well-built and ${value}.",
        "Has a ${value} construction.",
        "${product} is sturdy and ${value}.",
    ],
    "usage": [
        "Very ${value} to operate.",
        "Found it ${value} for daily use.",
        "Designed to be ${value}.",
        "Using the ${product} is quite ${value}.",
        "Offers a ${value} experience.",
    ],
    "material": [
        "Made from ${value} materials.",
        "The ${value} feel is evident.",
        "Constructed with ${value} components.",
        "Has a ${value} texture.",
        "The material quality is ${value}.",
    ],
    "comfort": [
        "Extremely ${value} to use.",
        "Offers a ${value} experience.",
        "Designed for ${value}.",
        "The ${product} provides ${value}.",
        "Feels ${value} during use.",
    ],
    "design": [
        "Features a ${value} design.",
        "The ${value} look is appealing.",
        "Has a ${value} aesthetic.",
        "The design of ${product} is quite ${value}.",
        "Showcases a ${value} style.",
    ],
    "experience": [
        "Provides an ${value} experience.",
        "Using it was quite ${value}.",
        "Overall, an ${value} product.",
        "The ${product} offers an ${value} usage.",
        "Had an ${value} time with it.",
    ],
    "durability": [
        "Very ${value} over time.",
        "Built to be ${value}.",
        "Shows ${value} after extended use.",
        "The ${product} is known for its ${value}.",
        "Offers ${value} in daily wear and tear.",
    ],
    "convenience": [
        "Extremely ${value} to carry around.",
        "Designed for ${value}.",
        "Offers ${value} in usage.",
        "The ${product} is quite ${value}.",
        "Provides ${value} for users.",
    ],
    "packaging": [
        " The packaging was ${value}.",
        " I liked how the item was ${value}.",
        " Packaged ${value}, very convenient.",
    ],
    "promotion": [
        " I got it during a ${value}, which was nice.",
        " Took advantage of the ${product} ${value} deal.",
        " Purchased it with a ${value} offer.",
    ],
}

NEGATIVE_DESCRIPTOR_TEMPLATES = {
    "price": [
        "At ${value}, not worth it.",
        "Price-wise, ${value} feels overpriced.",
        "Too expensive at ${value} for what it offers.",
        "Considering the quality, ${value} is not reasonable.",
        "${value} is not a good investment.",
    ],
    "taste": [
        "The taste is ${value} and disappointing.",
        "I found ${product}'s flavor to be ${value}, not enjoyable.",
        "Tastes ${value}, which I disliked.",
        "${product} has a ${value} flavor that I cannot recommend.",
    ],
    "texture": [
        "The texture is ${value} and unpleasant.",
        "Found ${product} ${value} when using it. Not good.",
        "Feels ${value} in a bad way.",
        "Texture is ${value}, which I disliked.",
    ],
    "scent": [
        "${product} smells ${value} and off-putting.",
        "The ${value} scent is too strong or unpleasant.",
        "Has a ${value} aroma I did not like.",
    ],
    "performance": [
        "Performance-wise, it's ${value} and frustrating.",
        "It performs ${value}, not satisfactory.",
        "The ${product} is ${value} in operation.",
    ],
    "build": [
        "The build quality is ${value} and fragile.",
        "Feels ${value} and poorly constructed.",
        "${product} is ${value} and cheap.",
    ],
    "usage": [
        "Very ${value} to operate, frustrating to use.",
        "Found it ${value} for daily use, not convenient.",
        "Using ${product} is quite ${value}, disappointing.",
    ],
    "material": [
        "Made from ${value} materials, low-quality.",
        "The ${value} feel is unpleasant.",
        "Constructed with ${value} components, feels cheap.",
    ],
    "comfort": [
        "Extremely ${value} to use, uncomfortable.",
        "Offers a ${value} experience, not pleasant.",
        "${product} provides ${value}, disappointing.",
    ],
    "design": [
        "Features a ${value} design, unattractive.",
        "The ${value} look is unappealing.",
        "Has a ${value} style that is impractical.",
    ],
    "experience": [
        "Provides a ${value} experience, not enjoyable.",
        "Using it was ${value}, frustrating overall.",
        "${product} offers a ${value} usage, disappointing.",
    ],
    "durability": [
        "Very ${value}, breaks easily.",
        "Built to be ${value}, not lasting.",
        "Shows ${value} after short use.",
    ],
    "convenience": [
        "Extremely ${value} to carry around, inconvenient.",
        "Designed for ${value}, hard to use.",
        "${product} is ${value}, not user-friendly.",
    ],
    "packaging": [
        "The packaging was ${value}, not satisfactory.",
        "Item was ${value} packed, poorly handled.",
        "Packaging felt ${value}, disappointing.",
    ],
    "promotion": [
        "Got it during a ${value}, but not worth it.",
        "The ${product} ${value} deal was disappointing.",
        "Purchased with ${value}, felt like a bad deal.",
    ],
}

STATUS = ["active", "discontinued", "promotion"]

positive_adjectives = [
    "excellent",
    "amazing",
    "great",
    "fantastic",
    "high-quality",
    "perfect",
    "superb",
    "wonderful",
    "impressive",
    "top-notch",
    "outstanding",
]

negative_adjectives = [
    "disappointing",
    "poor",
    "terrible",
    "low-quality",
    "bad",
    "unsatisfactory",
    "inferior",
    "flawed",
    "subpar",
    "mediocre",
    "unpleasant",
]

neutral_phrases = [
    "average",
    "okay",
    "fine",
    "nothing special",
    "acceptable",
    "decent",
    "passable",
    "satisfactory",
    "moderate",
    "so-so",
]

positive_verbs = [
    "love",
    "enjoyed",
    "liked",
    "appreciated",
    "recommend",
    "adore",
    "favor",
    "admire",
    "cherish",
    "value",
]

negative_verbs = [
    "disliked",
    "regret buying",
    "was unhappy with",
    "would not buy again",
    "complain about",
    "detest",
    "cannot recommend",
    "feel let down by",
    "avoid",
    "beware of",
]

neutral_verbs = ["found", "tried", "tested", "used", "experienced"]

mention_types = [
    "none",
    "name",
    "price",
    "taste",
    "texture",
    "scent",
    "performance",
    "build",
    "usage",
    "material",
    "comfort",
    "design",
    "experience",
    "durability",
    "convenience",
    "packaging",
    "promotion",
]


def generate_mention_text(mention_type, product_name, value, sentiment, price=None):
    if sentiment == "positive" or sentiment == "neutral":
        if mention_type in POSITIVE_DESCRIPTOR_TEMPLATES and value is not None:
            template = random.choice(POSITIVE_DESCRIPTOR_TEMPLATES[mention_type])
            return template.replace("${value}", str(value)).replace(
                "${product}", product_name
            )
    elif sentiment == "negative":
        if mention_type in NEGATIVE_DESCRIPTOR_TEMPLATES and value is not None:
            template = random.choice(NEGATIVE_DESCRIPTOR_TEMPLATES[mention_type])
            return template.replace("${value}", str(value)).replace(
                "${product}", product_name
            )
    return ""


def generate_review(product_name, price, sentiment=None):
    if sentiment is None:
        sentiment = random.choices(
            ["positive", "neutral", "negative"], weights=[0.6, 0.2, 0.2]
        )[0]

    if sentiment == "negative":
        descriptors_pool = NEGATIVE_CATEGORY_DESCRIPTORS.get(category, {}).copy()
    elif sentiment == "positive":
        descriptors_pool = POSITIVE_CATEGORY_DESCRIPTORS.get(category, {}).copy()
    elif sentiment == "neutral":
        descriptors_pool = NEUTRAL_CATEGORY_DESCRIPTORS.get(category, {}).copy()

    descriptor_values = {}
    for d_type, options in descriptors_pool.items():
        if options:
            descriptor_values[d_type] = random.choice(options)

    for special in ["packaging", "promotion"]:
        if special not in descriptor_values or random.random() < 0.3:
            descriptor_values[special] = random.choice(
                GLOBAL_DESCRIPTORS[special].get(
                    sentiment, GLOBAL_DESCRIPTORS[special]["neutral"]
                )
            )

    mention_types = random.sample(
        list(descriptor_values.keys()), k=min(2, len(descriptor_values))
    )
    sentences = []

    for mention_type in mention_types:
        value = descriptor_values.get(mention_type)
        sentence = generate_mention_text(
            mention_type, product_name, value, sentiment, price
        )
        if sentence:
            sentences.append(sentence)

    mention_text = " ".join(sentences)

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
        f"{product_name} really impressed me. {random.choice(positive_verbs).capitalize()} it!{mention_text}",
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
        f"{product_name} is acceptable for the price.{mention_text}",
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
        f"Very {random.choice(negative_adjectives)}! {product_name} is disappointing.{mention_text}",
    ]

    if sentiment == "positive":
        text = random.choice(positive_templates)
        stars = random.randint(4, 5)
    elif sentiment == "neutral":
        text = random.choice(neutral_templates)
        stars = 3
    else:
        text = random.choice(negative_templates)
        stars = random.randint(1, 2)

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
        "love": "luv",
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
        "review_date": fake.date_between(
            start_date="-6M", end_date="today"
        ).isoformat(),
    }

    return review


products = []
product_ids = []

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
        category_name = category_name.replace("a", "@").replace("o", "0")

    # Prices
    selling_price: Optional[float] = round(random.uniform(1.5, 100), 2)
    if selling_price is not None:
        cost_price = round(selling_price * random.uniform(0.5, 0.95), 2)

    status = random.choices(STATUS, weights=[0.85, 0.05, 0.10])[0]

    # Stock labels (with inconsistencies)
    stock = random.choices(
        ["in stock", "instock", "OUT OF STOCK", None], weights=[0.7, 0.1, 0.15, 0.05]
    )[0]

    # Introduce missing price randomly
    if random.random() < 0.05:
        selling_price = None

    review_count = random.randint(MIN_REVIEWS, MAX_REVIEWS)
    reviews = [generate_review(name, selling_price) for _ in range(review_count)]

    for review in reviews:
        products.append(
            {
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
                "review_date": review["review_date"],
            }
        )

df = pd.DataFrame(products)
df.to_csv("data_generation/raw_data/products_raw.csv", index=False)
print("products_raw.csv file generated")
