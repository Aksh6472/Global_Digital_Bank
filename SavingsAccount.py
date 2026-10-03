# package com.gdb.domain
from exceptions import *
from Account import Account

class SavingsAccount(Account):
    # ===== Constants =====
    MINIMUM_BALANCE = 500.0
    ACCOUNT_TYPE = "Savings"
    INTEREST_RATE = 4.0  # 4% per annum

    # ===== Constructor =====
    def __init__(self, accountNumber, name, age, initialBalance):
        # Raises ValueError
        super().__init__(accountNumber, name, age, initialBalance)

    # ===== Abstract Method Implementations =====
    def getMinimumBalance(self):
        return self.MINIMUM_BALANCE

    def getAccountType(self):
        return self.ACCOUNT_TYPE

    # ===== Savings-Specific Methods =====
    def calculateInterest(self, years):
        if years < 0:
            raise ValueError("Years must be non-negative")
        return self.getBalance() * (self.INTEREST_RATE / 100) * years

    def getInterestRate(self):
        return self.INTEREST_RATE
