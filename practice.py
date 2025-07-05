reviews = {
    "Ayesha": "The service was excellent and staff was awesome.",
    "Bilal": "It was a bad experience, the food was cold.",
    "Sarah": "Everything was okay, nothing special.",
    "Ali": "Good environment and tasty food!",
    "Zara": "Worst service ever, I won't come again.",
}

negative_reviews = 0
positive_reviews = 0
neutral_reviews = 0

for name, comments in reviews.items():
    print(f"\nName: {name}")
    print(f"Comments: {comments}")

    comments_lower = comments.lower()

    if (
        "excellent" in comments_lower
        or "good" in comments_lower
        or "awesome" in comments_lower
    ):
        positive_reviews += 1
    elif (
        "bad" in comments_lower
        or "worst" in comments_lower
    ):
        negative_reviews += 1
    else:
        neutral_reviews += 1

print("=" * 30)
print("\n📊 Summary Report")
print("-" * 30)
print(f"Positive Reviews: {positive_reviews}")
print(f"Negative Reviews: {negative_reviews}")
print(f"Neutral Reviews: {neutral_reviews}")
