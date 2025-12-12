class BankAccount:
    """
    Base class for all account types.
    Holds common functionality like deposit, withdraw, and balance handling.
    """
    def __init__(self, holder_name, balance=0):
        # Using protected attributes so child classes can safely access/modify.
        self._holder_name = holder_name
        self._balance = balance

    def deposit(self, amount):
        # Basic validation for realistic behavior.
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False

        self._balance += amount
        return True

    def withdraw(self, amount):
        # Prevent negative or zero withdrawals.
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        # Standard account cannot go below zero.
        if amount > self._balance:
            print("Insufficient funds!")
            return False

        self._balance -= amount
        return True

    def display_balance(self):
        print(f"{self._holder_name}'s balance is: ${self._balance:.2f}")

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    """
    Savings account with interest feature.
    """
    def __init__(self, holder_name, balance=0, interest_rate=0.01):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Interest gets added as a normal deposit.
        interest = self._balance * self.interest_rate
        self.deposit(interest)

    def display_balance(self):
        # Add some context for the output.
        print("Savings Account Summary:")
        super().display_balance()


class CurrentAccount(BankAccount):
    """
    Current/Checking account that supports overdraft.
    """
    def __init__(self, holder_name, balance=0, overdraft_limit=500):
        super().__init__(holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Overdraft-enabled withdrawal.
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        # Allow going below zero, but up to the overdraft limit.
        if amount > self._balance + self.overdraft_limit:
            print("Overdraft limit exceeded!")
            return False

        self._balance -= amount
        return True


def transfer(from_account, to_account, amount):
    """
    Handles fund transfer between two accounts.
    Withdraw succeeds → then deposit.
    This avoids situations where only one side completes.
    """
    if from_account.withdraw(amount):
        to_account.deposit(amount)
        print(
            f"Transferred ${amount} from {from_account._holder_name} "
            f"to {to_account._holder_name}."
        )
    else:
        print("Transfer failed.")


def main():
    # Creating sample accounts to test the workflow.
    john_savings = SavingsAccount("John Doe", 1000, 0.05)
    jane_current = CurrentAccount("Jane Smith", 500, 300)

    # Basic operations.
    john_savings.deposit(500)
    john_savings.withdraw(200)
    john_savings.apply_interest()  # Adds 5% interest.

    # Attempt transfer.
    transfer(john_savings, jane_current, 700)

    # Final state summary.
    john_savings.display_balance()
    jane_current.display_balance()


if __name__ == "__main__":
    main()
