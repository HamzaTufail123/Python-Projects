def pin_verify():
    attempts = 0
    correct_pin = "1234"

    while attempts < 3:
        user_input = input("Enter 4-digit PIN: ")

        if len(user_input) != 4 or not user_input.isdigit():
            print("Invalid user PIN.")
            attempts += 1

        elif user_input == correct_pin:
            print(
                f"You Entered correct pin: '{correct_pin}' in {attempts + 1} attempts. System login Successfully."
            )
            break

        else:
            print("Incorrect Pin.")
            attempts += 1
    if attempts == 3:
        print("Your account has been locked! ")


pin_verify()
