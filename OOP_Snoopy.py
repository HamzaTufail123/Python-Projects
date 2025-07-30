class Snoopy:
    total_customers = 0

    def __init__(self, name, Token_no):
        self.name = name
        self.Token_no = Token_no
        self.item_dict = {}
        Snoopy.total_customers += 1

    def input_items(self, pdt_name, pdt_price, pdt_qty):
        self.item_dict[pdt_name] = [pdt_price, pdt_qty]

    def display(self):
        print(f"Customer Name: {self.name}")
        print(f"Token #no: {self.Token_no}")
        print(f"Purchase Item: ")

        grand_total = 0
        for name, data in self.item_dict.items():
            price, qty = data
            total = price * qty

            print(f"- {name} | Price: Rs.{price} | Qty: {qty} | Total: {total}")
            grand_total += total

            if qty > 5:
                discount = price * 0.1
                reduce_amount = discount - price
                total -= discount
                print(f"Discount Applied: {discount}")
            else:
                print("NO discount.")
            grand_total += total


        
        print(f"\nGrand Total : {grand_total}")

name = input("Enter Customer Name: ").capitalize().strip()
Token_no = input("Enter Customer Token #no: ").strip()

customer = Snoopy(name, Token_no)

num = int(input("How many items did you buy: ").strip())
for i in range(num):
    print("\nEntered Items Detailed: ")
    pdt_name = input("Enetr item name: ").capitalize().strip()
    pdt_price = int(input(f"Enter price of '{pdt_name}': ").strip())
    pdt_qty = int(input(f"Enter '{pdt_name}' quantity: ").strip())
    customer.input_items(pdt_name, pdt_price, pdt_qty)

customer.display()
print(f"\nTotal customer: {Snoopy.total_customers}")

    
