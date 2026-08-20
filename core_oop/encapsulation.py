"""Encapsulation: expose safe operations instead of raw state.

Without encapsulation, callers can change a balance directly and create an
invalid account. The solution is to keep the balance behind methods that
validate each operation, then expose only the read-only value through a
property.
"""


class UnsafeBankAccount:
    """A deliberately unsafe version that exposes its state directly."""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance


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
    print("WITHOUT ENCAPSULATION")
    unsafe_account = UnsafeBankAccount("Asha", 100)
    unsafe_account.balance += 50
    unsafe_account.balance -= 250
    print(f"Anyone can create an invalid balance: {unsafe_account.balance}")

    print("\nWITH ENCAPSULATION")
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
