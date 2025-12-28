import random
from datetime import timedelta
from typing import Optional

import pandas as pd
from config import (
    BRANDS,
    CATEGORIES,
    CATEGORY_ITEMS,
    GLOBAL_DESCRIPTORS,
    MAX_REVIEWS,
    MIN_REVIEWS,
    NEGATIVE_ADJECTIVES,
    NEGATIVE_CATEGORY_DESCRIPTORS,
    NEGATIVE_DESCRIPTOR_TEMPLATES,
    NEGATIVE_VERBS,
    NEUTRAL_CATEGORY_DESCRIPTORS,
    NEUTRAL_PHRASES,
    NEUTRAL_VERBS,
    NUM_PRODUCTS,
    POSITIVE_ADJECTIVES,
    POSITIVE_CATEGORY_DESCRIPTORS,
    POSITIVE_DESCRIPTOR_TEMPLATES,
    POSITIVE_VERBS,
)
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)


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
        f"{random.choice(POSITIVE_VERBS).capitalize()} this product! It's {random.choice(POSITIVE_ADJECTIVES)}.{mention_text}",
        f"This product is {random.choice(POSITIVE_ADJECTIVES)} and I {random.choice(POSITIVE_VERBS)} it.{mention_text}",
        f"Absolutely {random.choice(POSITIVE_ADJECTIVES)}! {random.choice(POSITIVE_VERBS).capitalize()} it.{mention_text}",
        f"I {random.choice(POSITIVE_VERBS)} {product_name}. Truly {random.choice(POSITIVE_ADJECTIVES)}.{mention_text}",
        f"{product_name} exceeded my expectations. {random.choice(POSITIVE_VERBS).capitalize()} it!{mention_text}",
        f"I've been using {product_name} for a while and it's {random.choice(POSITIVE_ADJECTIVES)}.{mention_text}",
        f"{random.choice(POSITIVE_VERBS).capitalize()} this! {product_name} is {random.choice(POSITIVE_ADJECTIVES)}.",
        f"Highly {random.choice(['recommended', 'suggested', 'endorsed'])}! {product_name} is {random.choice(POSITIVE_ADJECTIVES)}.{mention_text}",
        f"Can't get enough of {product_name}! It's {random.choice(POSITIVE_ADJECTIVES)}.{mention_text}",
        f"One of the best purchases I've made this year! {product_name} is {random.choice(POSITIVE_ADJECTIVES)}.{mention_text}",
        f"{product_name} really impressed me. {random.choice(POSITIVE_VERBS).capitalize()} it!{mention_text}",
    ]

    neutral_templates = [
        f"This product is {random.choice(NEUTRAL_PHRASES)}.{mention_text}",
        f"I {random.choice(NEUTRAL_VERBS)} {product_name} to be {random.choice(NEUTRAL_PHRASES)}.{mention_text}",
        f"{product_name} is {random.choice(NEUTRAL_PHRASES)}, nothing fancy.{mention_text}",
        f"Overall, {product_name} seems {random.choice(NEUTRAL_PHRASES)}.{mention_text}",
        f"{product_name} is okay. {random.choice(['Nothing special', 'Meets expectations', 'Average quality'])}.{mention_text}",
        f"Using {product_name} was {random.choice(NEUTRAL_PHRASES)}. Would buy again? Not sure.{mention_text}",
        f"Just tried {product_name}. It's {random.choice(NEUTRAL_PHRASES)}.{mention_text}",
        f"{product_name} serves its purpose. {random.choice(NEUTRAL_PHRASES).capitalize()} quality.{mention_text}",
        f"Nothing extraordinary about {product_name}. It's {random.choice(NEUTRAL_PHRASES)}.{mention_text}",
        f"{product_name} is acceptable for the price.{mention_text}",
    ]

    negative_templates = [
        f"{random.choice(NEGATIVE_VERBS).capitalize()} {product_name}. It's {random.choice(NEGATIVE_ADJECTIVES)}.{mention_text}",
        f"I {random.choice(NEGATIVE_VERBS)} this product. {product_name} felt {random.choice(NEGATIVE_ADJECTIVES)}.{mention_text}",
        f"Unfortunately, {product_name} is {random.choice(NEGATIVE_ADJECTIVES)}. {random.choice(NEGATIVE_VERBS).capitalize()} it.{mention_text}",
        f"{product_name} did not meet my expectations. {random.choice(NEGATIVE_VERBS).capitalize()} it.{mention_text}",
        f"Really {random.choice(NEGATIVE_ADJECTIVES)} experience with {product_name}.{mention_text}",
        f"{product_name} disappointed me. {random.choice(NEGATIVE_VERBS).capitalize()} it!{mention_text}",
        f"Not impressed with {product_name}. It's {random.choice(NEGATIVE_ADJECTIVES)}.{mention_text}",
        f"{product_name} didn't live up to the hype. {random.choice(NEGATIVE_VERBS).capitalize()} this product.{mention_text}",
        f"{random.choice(NEGATIVE_ADJECTIVES).capitalize()} quality. I {random.choice(NEGATIVE_VERBS)} {product_name}.{mention_text}",
        f"{product_name} is subpar. {random.choice(NEGATIVE_VERBS).capitalize()} it.{mention_text}",
        f"Very {random.choice(NEGATIVE_ADJECTIVES)}! {product_name} is disappointing.{mention_text}",
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

    status = random.choices(
        ["active", "discontinued", "promotion"], weights=[0.85, 0.05, 0.10]
    )[0]

    promotion_type = random.choices(
        [None, "Buy One Get One", "Discounted"], weights=[0.85, 0.05, 0.10]
    )[0]

    promotion_discount_percentage = None
    if promotion_type == "Discounted":
        promotion_discount_percentage = random.randint(5, 20)
    elif promotion_type == "Buy One Get One":
        promotion_discount_percentage = 50

    promotion_start_date = None
    promotion_end_date = None
    discontinuation_date = None

    if status == "promotion":
        promotion_start_date = fake.date_between(start_date="-3M", end_date="-1M")
        promotion_end_date = promotion_start_date + timedelta(weeks=1)
    elif status == "discontinued":
        discontinuation_date = fake.date_between(start_date="-3M", end_date="today")

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
                "promotion_type": promotion_type,
                "promotion_start_date": promotion_start_date,
                "promotion_end_date": promotion_end_date,
                "discontinuation_date": discontinuation_date,
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
