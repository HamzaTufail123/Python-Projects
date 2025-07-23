def Quiz_Builder():
    mcqs = []

    question_quantity_input = input("How many question would you add? ")

    if not question_quantity_input.isdigit():
        print("Invalid user input.enter a number.")
        return []
    
    question_quantity = int(question_quantity_input)

    for i in range(question_quantity):

        print(f"\nQuestion # {i + 1}")
        question_text = input("Type question: ")

        option = {}
        option["A"] = input("Option A: ")
        option["B"] = input("Option B: ")
        option["C"] = input("Option C: ")
        option["D"] = input("Option D: ")

        correct_option = input("Enter correct option (A/B/C/D): ").upper()

        if correct_option not in ["A", "B", "C", "D"]:
            print("Invalid input. Skipping this question. ")
            continue

        mcq = {"question": question_text, "options": option, "answer": correct_option}

        mcqs.append(mcq)
    return mcqs


def MCQs(mcqs):
    print("-" * 40)
    score = 0
    for mcq in mcqs:
        print("\n" + mcq["question"])
        for key, value in mcq["options"].items():
            print(f"{key}) {value} ")

        user_input = input("Enter correct option (A/B/C/D): ").upper()
        if user_input not in ["A", "B", "C", "D"]:
            print("Invalid option. Skipping this question. ")
            continue
        if user_input == mcq["answer"]:
            print("\n Correct. ")
            score += 1
        else:
            print(f"Wrong answer! Correct option is: {mcq['answer']}")

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
        grade = "Fail"

    print("=" * 40)
    print(f"Grade: {grade}")
    print(f"Percentage: {average:.2f}")
    print("Game over! ")


while True:
    question = Quiz_Builder()
    MCQs(question)

    re_start = input("Would you like play again? ").lower()
    if re_start != "yes":
        print("Thanks to play this intresting game. ")
        break
