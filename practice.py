# user_num = int(input("Enter a number: "))
# def func(user_num):
#     factorial = 1
#     for i in range(1, user_num + 1):
#         factorial *= i
#     return factorial
# print(f"Factorial of {user_num} is: {func(user_num)}")


# user_input = int(input("Enter a number: "))
# def fabonachi(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fabonachi(n - 1) + fabonachi(n - 2)
# print(f"Fabonachi Series up to {fabonachi} terms.")
# for i in range(user_input):
#     print(fabonachi(i), end=" ")

# *******************************************************
account_data = {}
transaction_log = []


def create_account():
    name = input("Enter your name: ")
    balance = int(input("Enter your balance: "))
    account_data["name"] = name
    account_data["balance"] = balance
    print(f"Welcome {name}, your account is created with Rs.{balance}")


def deposit():
    amount = int(input("Enter an amount: "))
    account_data["balance"] += amount
    transaction_log.append(f"Deposit  Rs.{amount}")


def withdraw():
    amount = int(input("Enter your withdraw amount: "))
    if amount > account_data["balance"]:
        print("Insufficient Funds.")
    else:
        account_data["balance"] -= amount
        transaction_log.append(f"Withdraw Rs.{amount}")


def view_balance():
    print(f"Current Balance: Rs.{account_data['balance']}")


def save_history():
    with open("practice.txt", "w", encoding="utf-8") as f:
        f.write(f"User: {account_data['name']}\n")
        f.write(f"Final Balance: {account_data['balance']}\n")
        f.write("Transaction:\n")
        for entry in transaction_log:
            f.write(f"* {entry}\n")



create_account()

while True:
    print("\n1. Deposit \n2. Withdraw \n3. Check balance \n4. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        view_balance()
    elif choice == "4":
        save_history()
        print("Thanks for using smart bank.")
        break
    else:
        print("Invalid Option.")
