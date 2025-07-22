def Quiz_Game():
    import random

    mcqs = [
        {
            "question": "What is the capital of pakistan?",
            "options": {"A": "Karachi", "B": "Lahore", "C": "Multan", "D": "Islamabad"},
            "answer": "D",
        },
        {
            "question": "What is biggest city of Pakistan?",
            "options": {"A": "Multan", "B": "Gujrawala", "C": "Karachi", "D": "Lahore"},
            "answer": "C",
        },
        {
            "question": "What is the capital of Russia?",
            "options": {"A": "Moscow", "B": "St. Peterberg", "C": "Kazan", "D": "Gurzni"},
            "answer": "A",
        },
    ]
    random.shuffle(mcqs)
    score = 0
    for mcq in mcqs:

        print(mcq["question"])

        for key, value in mcq["options"].items():
            print(f"{key}) {value}")

        user_input = input("Enter right option (A/B/C/D): ").upper()
        if user_input not in ["A", "B", "C", "D"]:
            print("Invaild opton. skipping this mcq. ")
            continue
        if user_input == mcq["answer"]:
            print("Correct\n")
            score += 1
        else:
            print(f"Wrong answer. Correct option is: {mcq['answer']}")

    average = score / len(mcqs) * 100
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    elif average >= 40:
        grade = "F"

    else:
        print("Invalid user input. ")

    print("-" * 10, "Result", "-" * 10)
    print(f"Percentage: {average:.2f}%")
    print(f"Grade : {grade}")
    print(f"Game over!")

while True:
    Quiz_Game()

    re_start = input("Do wanna play again? (yes/no): ").lower()
    if re_start != "yes":
        print("\nThanks to play this intresting game.")
        break




