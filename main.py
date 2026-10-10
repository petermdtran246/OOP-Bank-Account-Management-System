class InsufficientFundsError(Exception):
    """Raised when a withdrawal amount exceeds the account balance."""
    pass


class BankAccount:
    # Class-level counter shared across all BankAccount instances
    acc_counter = 100

    def __init__(self, name: str, balance: float):
        """Initialize a new bank account.
        
        Args:
            name (str): Customer's name (Public).
            balance (float): Initial balance (Private).
        """
        self.name = name
        BankAccount.acc_counter += 1
        
        # Private attributes (Name Mangling applied)
        self.__acc = BankAccount.acc_counter
        self.__balance = balance

    def deposit(self, amount: float) -> float:
        """Deposit funds into the account and return the updated balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float) -> None:
        """Withdraw funds from the account.
        
        Raises:
            InsufficientFundsError: If amount exceeds the available balance.
        """
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
        else:
            raise InsufficientFundsError("Not enough funds to complete transaction.")

    def get_balance(self) -> float:
        """Getter method to view the current balance safely."""
        return self.__balance

    def details(self) -> tuple:
        """Return full account summary as a tuple: (name, account_number, balance)."""
        return self.name, self.__acc, self.__balance


if __name__ == "__main__":
    # Create account instance
    am1 = BankAccount("Jame", 2500)

    # Perform transactions
    am1.withdraw(500)

    # Display account summary
    print(f"Customer Name  : {am1.name}")
    print(f"Account Counter: {am1.acc_counter}")
    print(f"Current Balance: ${am1.get_balance():,.2f}")
