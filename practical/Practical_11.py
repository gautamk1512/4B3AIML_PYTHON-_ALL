# Question:
# A program that models a bank account, with classes for the account, the customer, and the bank.

# Explanation:
# This program uses Object-Oriented Programming (OOP).
# - `Customer` class holds personal details.
# - `Account` class manages balance, deposits, and withdrawals.
# - `Bank` class manages multiple accounts.

# Code Breakdown:
# 1. Define `Customer` class with `__init__` to store name and ID.
# 2. Define `Account` class with `__init__` linking a customer and starting balance.
# 3. Define `deposit` method in `Account` to add funds.
# 4. Define `withdraw` method in `Account` to remove funds if sufficient.
# 5. Define `Bank` class with list `accounts` to store Account objects.
# 6. Define `add_account` method in `Bank` to register new accounts.
# 7. Create instances: `cust` (Customer), `acc` (Account), `my_bank` (Bank).
# 8. Perform operations: Add account to bank, deposit money, withdraw money.

class Customer:
    # 1. Initialize Customer
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

class Account:
    # 2. Initialize Account linked to a Customer
    def __init__(self, customer, balance=0):
        self.customer = customer
        self.balance = balance

    # 3. Deposit Method
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")

    # 4. Withdraw Method
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")

class Bank:
    # 5. Initialize Bank
    def __init__(self, name):
        self.name = name
        self.accounts = []

    # 6. Add Account to Bank
    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account for {account.customer.name} added to {self.name}.")

# 7. Create Objects (Usage)
cust = Customer("John Doe", "C001")
acc = Account(cust, 1000)
my_bank = Bank("Python Bank")

# 8. Perform Operations
my_bank.add_account(acc)
acc.deposit(500)
acc.withdraw(200)
