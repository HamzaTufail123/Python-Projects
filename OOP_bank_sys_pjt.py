class Bank:
    def __init__(self, name, acc_number, pin):
        self.name = name
        self.acc_number = acc_number
        self.pin = pin
        self.balance = 0

    def verify_pin(self):
        entered_pin  = input("Enter user pin: ").strip()
        return entered_pin == self.pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs.{amount} deposited successfully. ")

        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance. ")

        elif amount <= 0:
            print("Invalid with draw amount.")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Account Holder Name: ", self.name)
        print(f"Account Number: ", self.acc_number)
        print(f"Current Balance: ", self.balance)

user_name = input("Enter user name: ").strip().capitalize()
user_Account_number = input("Enter user account number: ").strip()
user_pin = input("Set you 4-digit PIN: ").strip()
if len(user_pin ) != 4:
    print("Invalid pin!")
user1 = Bank(user_name, user_Account_number, user_pin)

while True:

    print("\n1. Deposit \n2. Withdraw \n3. Check Balance \n4. Exit")
    options = input("Choose option: ")
    if options == "1":
        if user1.verify_pin():
            amt = int(input("Enter amount to deposit money: "))
            user1.deposit(amt)
        else:
            print("Wrong pin! ")
    elif options == "2":
        amt = int(input("Enter amount to withdraw: "))
        user1.withdraw(amt)
    elif options == "3":
        user1.check_balance()
    elif options == "4":
        print("Exiting..")
        break
    else:
        print("Invalid choise. Try again.")


