# **************************************************************
contact_dict = {}


def add_contacts():
    user_name = input("Enter user name: ")
    user_contact = input("Enter a number: ")
    if len(user_name) == 10:
        contact_dict[user_name] = user_contact
        print(f"Contact added: {user_name} - {user_contact}")
    else:
        print(f"Entered number is wrong. ")


def search_contact():
    user_name = input("Enter user name to search: ")
    if user_name in contact_dict:
        print(f"Contact found: {user_name} - {contact_dict[user_name]}")
    else:
        print("Not found.")


def delete():
    user_name = input("Enter user name to delete: ")
    if user_name in contact_dict:
        del contact_dict[user_name]
        print(f"Contact '{user_name}' deleted successfully.")
    else:
        print(f"{user_name} not found in contact list.")


def view_all_contact():
    if not contact_dict:
        print("No contacts available.")
    else:
        print("All Contacts:")
        for name, number in contact_dict.items():
            print(f"Name: {name} | Contact: +92{number}")


def save_history():
    with open("practice_03.txt", "w", encoding="utf-8") as f:
        for name, number in contact_dict.items():
            f.write(f"{name}: +92{number}\n")
    print("Contacts saved to file.")


while True:
    print("\n======= Contact Book Menu =======")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Save History to File")
    print("6. Exit")

    choose = input("Enter option (1-6): ")

    if choose == "1":
        add_contacts()
    elif choose == "2":
        search_contact()
    elif choose == "3":
        delete()
    elif choose == "4":
        view_all_contact()
    elif choose == "5":
        save_history()
    elif choose == "6":
        print("Goodbye! Contact book closed.")
        break
    else:
        print("Invalid option. Try again.")
# **************************************************************

