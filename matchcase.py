#ATM MENU
balance=10000
print("-----ATM MENU-----")
print("1.Check Balance")
print("2.Deposit")
print("3.withdraw")
print("4.Exit")

choice=int(input("Enter your choice :"))

match choice:
    case 1:
        print("Current balance: ",balance)
    case 2:
        amount=int(input("Enter deposit amount :"))
        balance=balance+amount
        print("Deposit amount")
        print("Updated balance:",balance)
    case 3:
        amount=int(input("Enter withdrawal amount:"))
        if amount <= balance:
            balance=balance-amount
            print("withdrawal succesfull")
            print("Remaining balance:",balance)
        else:
            print("insufficient balance")
    case 4:
        print("Thanku you for using ATM")
    case _:
        print("Invalid choice")



# Restaurent Menu..
print("----- MENU -----")
print("1. Biryani")
print("2. Chicken 65")
print("3. Veg Pulao")
print("4. Butter Chicken")
print("5. Paneer Tikka")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Item : Biryani")
        print("Price : ₹250")
    case 2:
        print("Item : Chicken 65")
        print("Price : ₹180")
        print("Description : Crispy and spicy deep-fried chicken pieces.")
    case 3:
        print("Item : Veg Pulao")
        print("Price : ₹150")

    case 4:
        print("Item : Butter Chicken")
        print("Price : ₹280")
    case 5:
        print("Item : Paneer Tikka")
        print("Price : ₹200")
    case _:
        print("Invalid choice")