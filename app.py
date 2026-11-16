
class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    account = BankAccount(1000)
    print("Initial balance:", account.check_balance())
    account.deposit(500)
    print("After deposit:", account.check_balance())
    account.withdraw(200)
    print("Final balance:", account.check_balance())

