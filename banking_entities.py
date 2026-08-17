from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder_name, pin, balance=0.0):
        self.holder_name = holder_name
        self.pin = pin
        self._balance = float(balance)

    @property
    def holder_name(self):
        return self._holder_name

    @holder_name.setter
    def holder_name(self, value):
        if not value.strip():
            raise ValueError("Holder name cannot be empty!")
        self._holder_name = value

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, value):
        if not (value.isdigit() and len(value) == 4):
            raise ValueError("PIN must be exactly 4 digits!")
        self._pin = value

    @property
    def balance(self):
        return self._balance

    @property
    @abstractmethod
    def account_type(self):
        pass

    @abstractmethod
    def get_details(self):
        pass
# ---------------------------------------------------------------------------------------------------------

class SavingsAccount(BankAccount):
    @property
    def account_type(self):
        return "Savings"

    def get_details(self):
        return f"[Savings] Account Holder: {self.holder_name} | Balance: ₹{self.balance:.2f}"


class CurrentAccount(BankAccount):
    @property
    def account_type(self):
        return "Current"

    def get_details(self):
        return f"[Current] Account Holder: {self.holder_name} | Balance: ₹{self.balance:.2f}"


def account_factory(acc_type, name, pin, balance=0.0):
    mapping = {
        "Savings": SavingsAccount,
        "Current": CurrentAccount
    }
    target = mapping.get(acc_type)
    if target:
        return target(name, pin, balance)
    return None