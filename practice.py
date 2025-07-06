feedback_list = []
feedback_result = {}
positive_feedback = 0
negative_feedback = 0
neutral_feedback = 0

user_feedback_range = int(input("Enter range of feedbacks: "))

for i in range(user_feedback_range):
    feedback = input(f"Enter your feedback #{i + 1}: ").strip()
    feedback_list.append(feedback)

for j in feedback_list:
    feedback_lower = j.lower()
    if (
        "excellent" in feedback_lower
        or "good" in feedback_lower
        or "great" in feedback_lower
    ):
        positive_feedback += 1
        feedback_result[j] = "Positive"
    elif (
        "bad" in feedback_lower or "worst" in feedback_lower or "hard" in feedback_lower
    ):
        negative_feedback += 1
        feedback_result[j] = "Negative"
    else:
        neutral_feedback += 1
        feedback_result[j] = "Neutral"

print("=" * 30)

# Save to file
with open("practice.txt", "w", encoding="utf-8") as file:
    file.write("📊 Feedback Summary:\n")
    file.write(f"Positive: {positive_feedback}\n")
    file.write(f"Negative: {negative_feedback}\n")
    file.write(f"Neutral: {neutral_feedback}\n")
    file.write("\n📝 Feedback Details:\n")
    for fb, sentiment in feedback_result.items():
        file.write(f"• {fb} => {sentiment}\n")

print("✅ File 'practice.txt' saved successfully.")
