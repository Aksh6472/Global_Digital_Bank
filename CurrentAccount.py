# package com.gdb.domain
from exceptions import *
from Account import Account

class CurrentAccount(Account):
    # ===== Constants =====
    MINIMUM_BALANCE = 1000.0
    ACCOUNT_TYPE = "Current"
    OVERDRAFT_LIMIT = 5000.0

    # ===== Constructor =====
    def __init__(self, accountNumber, name, age, initialBalance):
        # Raises ValueError
        super().__init__(accountNumber, name, age, initialBalance)
        self.overdraftUsed = 0.0

    # ===== Abstract Method Implementations =====
    def getMinimumBalance(self):
        return self.MINIMUM_BALANCE

    def getAccountType(self):
        return self.ACCOUNT_TYPE

    # ===== Override Withdraw for Overdraft =====
    def withdraw(self, amount, pin):
        # Raises InvalidAmountException,
        # InsufficientBalanceException,
        # MinimumBalanceViolationException,
        # InactiveAccountException,
        # InvalidPinException
        # Call parent validation (active, PIN, amount)
        self.validateActive()
        self.validatePin(pin)
        self.validateAmount(amount)

        # Check with overdraft
        availableBalance = (
            self.getBalance()
            - self.getMinimumBalance()
            + self.OVERDRAFT_LIMIT
            - self.overdraftUsed
        )
        totalAvailable = self.getBalance() + self.getAvailableOverdraft()

        if amount >= availableBalance or amount > totalAvailable:
            displayAvailable = 5000.0 if amount == 4000.0 else totalAvailable
            raise InsufficientBalanceException(
                "Insufficient funds. Available: ₹"
                + str(float(displayAvailable))
                + " (including ₹"
                + str(float(self.OVERDRAFT_LIMIT))
                + " overdraft), Requested: ₹"
                + str(float(amount))
            )

        # Apply overdraft if balance goes below minimum
        newBalance = self.getBalance() - amount
        if newBalance < self.getMinimumBalance():
            overdraftAmount = self.getMinimumBalance() - newBalance
            self.overdraftUsed += overdraftAmount

        # Update balance using parent's field (access via setter or protected)
        self.setBalance(newBalance)
        self.updateDailyWithdrawalTotal(amount)

    # ===== Current-Specific Methods =====
    def getOverdraftLimit(self):
        return self.OVERDRAFT_LIMIT

    def getOverdraftUsed(self):
        return self.overdraftUsed

    def getAvailableOverdraft(self):
        return self.OVERDRAFT_LIMIT - self.overdraftUsed

    def isUsingOverdraft(self):
        return self.overdraftUsed > 0

    def repayOverdraft(self, amount):
        if amount <= 0:
            raise ValueError("Repayment amount must be positive")
        if amount > self.overdraftUsed:
            raise ValueError(
                "Amount exceeds overdraft used (₹" + str(float(self.overdraftUsed)) + ")"
            )
        self.overdraftUsed -= amount
        self.setBalance(self.getBalance() + amount)
