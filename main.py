from bank_manager import BankManager

def menu():
    print("\n" + "▪"*45)
    print("      ENTERPRISE BANKING MANAGEMENT SYSTEM     ")
    print("▪"*45)
    print("1. Open New Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. View Transaction History")
    print("6. Exit Shell")
    print("▪"*45)

def main():
    manager = BankManager()
    while True:
        menu()
        choice = input("Select processing option index (1-6) :: ").strip()
        if choice == "1":
            manager.create_account()
        elif choice == "2":
            manager.check_balance()
        elif choice == "3":
            manager.deposit()
        elif choice == "4":
            manager.withdraw()
        elif choice == "5":
            manager.view_statement()
        elif choice == "6":
            print("\n Database session terminated gracefully. Goodbye!")
            break
        else:
            print(" Exception: Choice index out of boundary context.")

if __name__ == "__main__":
    main()