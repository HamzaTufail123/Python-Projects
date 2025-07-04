tea_menu = {
    "Masala": 50,
    "Green": 60,
    "Black": 30,
    "Ginger": 70,
    "Milk": 80,
    "oolong": 90,
}

print("☕ Welcome to Hamza's Tea Shop ☕")
print("Here is our menu:\n")

for tea, price in tea_menu.items():
    print(f"{tea} Tea - Rs.{price}")

choice = input(f"\nWhich tea would you like? (e.g. Masala): ")
if choice in tea_menu:
    quantity = int(input(f"How many cups of {choice} tea would you like? "))
    total = tea_menu[choice] * quantity

    print("\n🧾 Receipt")
    print("-" * 20)
    print(f"Tea Type: {choice}")
    print(f"Quantity: {quantity}")
    print(f"Total: Rs.{total}")
    print("-" * 20)
    print("Thank you for visiting.")
else:
    print("Sorry, we don't have that tea today.")
