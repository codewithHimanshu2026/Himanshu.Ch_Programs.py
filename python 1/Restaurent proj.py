Menu={"Burger":60,"Pizza":100,"Pasta":70,"Coffe":100}

def display_Menu():
    print("----Menu Items----")

    for item,price in Menu.items():
        print(f"{item:<15} Rs. {price}")


def take_order():
    order={}

    while True:
        item=input("\nEnter item name:").title()

        if item in Menu:
            while True:
                try:
                    qty=int(input("Enter quantity of {item}:"))
                    if qty<=0:
                        print("Quantity must be more than 0.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number")

            order[item]=order.get(item,0) +qty
        else:
            print("Item are not Available")

        choice=input("Do you want to order more? (yes/no):").lower()
        if choice!="yes":
            break

        return order

def generate_bill(order):
    if not order:
        print("\nNo items ordered.")
        return

    print("\n-------BILL-------")
    total=0
    for item,qty in order.items():
        price=Menu[item]
        amount=price*qty
        total+=amount
        print(f"{item:<15} x{qty:<3} = Rs.{amount}")
    print("--------------------")
    print(f"{total:<20} Rs. {total}")
    print("--------------------")

def main():
    print("Welcome to Himanshu Restaurent")
    display_Menu()
    order=take_order()
    generate_bill(order)

main()