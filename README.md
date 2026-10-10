# Python OOP: Bank Account Management System

A robust, beginner-friendly implementation of Object-Oriented Programming (OOP) in Python simulating a banking management system. This project demonstrates core OOP concepts, including **Encapsulation (Private Attributes & Name Mangling)**, **Class-level Variables**, **Method Delegation**, and **Custom Exception Handling**.

---

## 📌 Project Overview

This project simulates a bank account system where each account holder has an automatically assigned unique account number, a name, and an encapsulated balance. It guarantees transactional integrity by disallowing overdrafts via custom exceptions and preventing external tampering with critical account data.

### Key Features:
1. **Auto-Incrementing Account Numbers:** Uses a class attribute (`acc_counter`) shared across all instances to generate unique identifiers automatically.
2. **Data Encapsulation (Private Attributes):** Protects sensitive attributes (`__acc`, `__balance`) from direct external access using Python's double-underscore name mangling.
3. **Robust Transactions:**
   - `deposit(amount)`: Adds funds and returns updated balance.
   - `withdraw(amount)`: Deducts funds with validation against overdrafts.
4. **Custom Exception Handling:** Raises a user-defined `InsufficientFundsError` whenever a withdrawal exceeds the available funds.

---

## 🚀 Source Code Implementation

```python
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
```

---

## 🧪 Expected Output

```text
Customer Name  : Jame
Account Counter: 101
Current Balance: $2,000.00
```

---

## 💡 Key OOP Concepts Explained

### 1. Class Attribute vs. Instance Attribute

| Attribute Type | Declaration | Scope | Purpose in this Project |
| :--- | :--- | :--- | :--- |
| **Class Attribute** | `acc_counter = 100` (outside `__init__`) | Shared globally by the class and all its objects | Acts as the bank's central ticket dispenser to guarantee unique sequential IDs (`101`, `102`, ...). |
| **Instance Attribute** | `self.name`, `self.__balance` | Unique to each individual object | Stores account-specific information for that particular customer. |

### 2. Private Attributes & Name Mangling (`__`)

* **Double Underscore (`__balance`):** Python automatically transforms `__balance` internally into `_BankAccount__balance`.
* **Why it matters:** Calling `am1.__balance` directly from outside the class raises an `AttributeError`. This protects the customer's funds from unauthorized direct manipulation (e.g., `am1.__balance = 999999` will not overwrite the real balance).
* **Controlled Access:** Users must interact via official transaction methods (`deposit()`, `withdraw()`, `get_balance()`).

### 3. Custom Exception (`InsufficientFundsError`)

Instead of silently failing or returning negative values, the system actively triggers an exception when invalid business conditions occur:

```python
class InsufficientFundsError(Exception):
    pass
```

Invoking `am1.withdraw(5000)` when balance is only `$2000` halts the unauthorized withdrawal and cleanly reports:
```text
InsufficientFundsError: Not enough funds to complete transaction.
```

---

## 🛠️ How to Run Locally

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the script using Python 3:

```bash
python bank_account.py
```
