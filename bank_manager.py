import db_handler
from banking_entities import account_factory

class BankManager:
    def create_account(self):
        try:
            print("\nSelect Account Type:")
            print("1. Savings Account")
            print("2. Current Account")
            type_choice = input("Enter choice index :: ").strip()
            
            type_map = {"1": "Savings", "2": "Current"}
            acc_type = type_map.get(type_choice)
            if not acc_type:
                print(" Invalid account type selection!")
                return

            name = input("Enter Account Holder Name :: ").strip()
            pin = input("Set 4-Digit Security PIN :: ").strip()
            initial_deposit = float(input("Enter Initial Deposit Amount :: ").strip())

            
            obj = account_factory(acc_type, name, pin, initial_deposit)
            if not obj:
                raise RuntimeError("Factory construction failure.")

            acc_num = db_handler.save_account(obj.holder_name, obj.account_type, obj.pin, obj.balance)
            if acc_num:
                print(f"\n Success: Account registered! Account Number: {acc_num}")
            else:
                print("\n Operation Failed: Database insertion error.")

        except ValueError as err:
            print(f" Input Integrity Violation: {err}")
        except Exception as system_fault:
            print(f" System Fault: {system_fault}")

    def _authenticate(self):
        try:
            acc_num = int(input("Enter Account Number :: ").strip())
            pin = input("Enter 4-Digit PIN :: ").strip()
            
            row = db_handler.fetch_account(acc_num)
            if row and row['pin'] == pin:
                return row
            print(" Authentication Failed: Invalid credentials.")
            return None
        except ValueError:
            print(" Input Error: Account number must be numeric.")
            return None

    def check_balance(self):
        acc = self._authenticate()
        if acc:
            print(f"\n[Account #{acc['account_number']}] Holder: {acc['holder_name']}")
            print(f"Current Available Balance: ₹{acc['balance']:.2f}")

    def deposit(self):
        acc = self._authenticate()
        if acc:
            try:
                amount = float(input("Enter Deposit Amount :: ").strip())
                if amount <= 0:
                    print(" Error: Amount must be greater than 0.")
                    return
                
                new_balance = float(acc['balance']) + amount
                if db_handler.update_balance(acc['account_number'], new_balance, "DEPOSIT", amount):
                    print(f" Deposit Successful! Updated Balance: ₹{new_balance:.2f}")
            except ValueError:
                print(" Invalid monetary input.")

    def withdraw(self):
        acc = self._authenticate()
        if acc:
            try:
                amount = float(input("Enter Withdrawal Amount :: ").strip())
                current_bal = float(acc['balance'])
                if amount <= 0:
                    print(" Error: Amount must be greater than 0.")
                    return
                if amount > current_bal:
                    print(" Transaction Denied: Insufficient Funds.")
                    return

                new_balance = current_bal - amount
                if db_handler.update_balance(acc['account_number'], new_balance, "WITHDRAWAL", amount):
                    print(f" Withdrawal Successful! Updated Balance: ₹{new_balance:.2f}")
            except ValueError:
                print(" Invalid monetary input.")

    def view_statement(self):
        acc = self._authenticate()
        if acc:
            records = db_handler.fetch_transactions(acc['account_number'])
            print(f"\n================ TRANSACTION HISTORY (#{acc['account_number']}) ================")
            if not records:
                print("No transactions logged yet.")
            for r in records:
                print(f"[{r['timestamp']}] {r['transaction_type']} - Amount: ₹{r['amount']:.2f}")
            print("=================================================================")