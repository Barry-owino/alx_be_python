#!/usr/bin/env python3

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount instance.
        :param initial_balance: The starting balance of the account (default is 0)
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account
        :param amount:Amount to deposit must be positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        :Parama mount: Amount to withdraw must be positive and not exceed balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.account_balance:
            raise ValueError("Insufficient funds.")
        self.account_balance -= amount

    def get_balance(self):
        """
        Return the current account balance.
        :return: current account balance.
        """
        return self.account_balance



