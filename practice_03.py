# **************************************************************
contact_dict = {}
location_dict = {}


def add_contact():
    user_name = input("Enter your name: ")
    user_contact = input("Enter user contact: ")  # fixed input
    user_email = input("Enter an user email: ")
    user_city = input("Enter your city: ")

    if len(user_contact) == 10 and user_contact.isdigit():
        contact_dict[user_name] = user_contact
        location_dict[user_email] = user_city
        print(f"Contact added: {user_name} - {user_contact}")
    else:
        print("Entered number is wrong.")


def search_contact(contact_dict, location_dict):
    user_name = input("Enter user name: ")
    user_email = input("Enter an user email: ")
    if user_name in contact_dict and user_email in location_dict:
        print(
            f"Contact found: {user_name} - {contact_dict[user_name]} Email Address: {user_email} - {location_dict[user_email]}"
        )
    else:
        print("Not found.")


def delete():
    user_name = input("Enter user name: ")
    user_email = input("Enter an user email: ")
    if user_name in contact_dict and user_email in location_dict:
        del contact_dict[user_name]
        del location_dict[user_email]
        print(f"Contact: {user_name} your Email: {user_email} deleted successfully.")
    else:
        print("User name not found.")


def veiw_all():
    if not contact_dict and not location_dict:
        print("No contacts and location available.")
    else:
        for name, number in contact_dict.items():
            print(f"Name: {name} | Contact: {number}")
        for email, location in location_dict.items():
            print(f"Email: {email} | Location: {location}")


def save_history():
    with open("practice_03.txt", "w", encoding="utf-8") as f:
        for name, number in contact_dict.items():
            f.write(f"{name}: +92{number}\n")
        for email, location in location_dict.items():
            f.write(f"{email}: {location}\n")
    print("Contacts saved to file.")


while True:
    print("=" * 50)
    print("1. add_contact")
    print("2. search_contact details")
    print("3. delete")
    print("4. view_all")
    print("5. save_history")
    print("6. Exit")

    choose = input("Enter option(1-6): ")
    if choose == "1":
        add_contact()
    elif choose == "2":
        search_contact(contact_dict, location_dict)
    elif choose == "3":
        delete()
    elif choose == "4":
        veiw_all()
    elif choose == "5":
        save_history()
    elif choose == "6":
        print("Good Bye! Contact Book Closed.")
        break
    else:
        print("Invalid option. Try again!")
