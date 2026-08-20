"""Live examples for encapsulation and controlled state changes."""


class BankAccount:
    def __init__(self, owner: str, opening_balance: float = 0):
        self.owner = owner
        self._balance = opening_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        self._require_positive(amount)
        self._balance += amount

    def withdraw(self, amount: float):
        self._require_positive(amount)
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount

    @staticmethod
    def _require_positive(amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")


def main():
    account = BankAccount("Asha", 100)
    account.deposit(50)
    account.withdraw(25)
    print(f"{account.owner}'s balance: {account.balance}")

    try:
        account.withdraw(200)
    except ValueError as error:
        print(f"Rejected invalid operation: {error}")


if __name__ == "__main__":
    main()
