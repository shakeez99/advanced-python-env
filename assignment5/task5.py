class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__owner = owner
        self.__balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Withdrawal must not exceed balance.")
        self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance

    def get_owner(self) -> str:
        return self.__owner


def main() -> None:
    acc = BankAccount("Damir", 1000)
    print("Owner:", acc.get_owner())
    print("Balance:", acc.get_balance())

    acc.deposit(500)
    print("After deposit:", acc.get_balance())

    acc.withdraw(300)
    print("After withdraw:", acc.get_balance())

if __name__ == "__main__":
    main()
