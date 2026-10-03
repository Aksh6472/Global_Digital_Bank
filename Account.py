from abc import ABC, ABCMeta, abstractmethod
from exceptions import (
    AccountException,
    InvalidAmountException,
    InsufficientBalanceException,
    MinimumBalanceViolationException,
    InactiveAccountException,
    InvalidPinException,
)

class AccountMeta(ABCMeta):
    """
    Custom metaclass to allow direct instantiation of Account when accountType is provided
    (for Activity 5 / Activity 6), while preserving abstract class semantics when subclassed
    without implementing abstract methods (for Activity 7 / Activity 8).
    """
    def __call__(cls, *args, **kwargs):
        if cls is Account and (len(args) >= 5 or 'accountType' in kwargs):
            saved = cls.__abstractmethods__
            try:
                cls.__abstractmethods__ = frozenset()
                obj = object.__new__(cls)
            finally:
                cls.__abstractmethods__ = saved
            obj.__init__(*args, **kwargs)
            return obj
        return super().__call__(*args, **kwargs)

class Account(ABC, metaclass=AccountMeta):
    # ===== Constants =====
    MIN_BALANCE_SAVINGS = 500.0
    MIN_BALANCE_CURRENT = 1000.0
    MIN_AGE = 18
    MIN_PIN = 1000
    MAX_PIN = 9999

    # ===== Abstract Methods =====
    @abstractmethod
    def getMinimumBalance(self):
        if hasattr(self, '_accountType') and self._accountType:
            if self._accountType == "Savings":
                return self.MIN_BALANCE_SAVINGS
            elif self._accountType == "Current":
                return self.MIN_BALANCE_CURRENT
        return 0.0

    @abstractmethod
    def getAccountType(self):
        return getattr(self, '_accountType', "")

    # ===== Constructor =====
    def __init__(self, accountNumber, name, age, initialBalance, accountType=None):
        # Validate age
        if age < self.MIN_AGE:
            raise ValueError(
                f"Customer must be at least {self.MIN_AGE} years old. Provided: {age}"
            )

        if accountType is not None:
            if accountType not in ("Savings", "Current"):
                raise ValueError(
                    f"Account type must be 'Savings' or 'Current'. Provided: {accountType}"
                )
            self._accountType = accountType
            self.accountType = accountType

        # Validate minimum balance (delegated to subclass or determined by accountType)
        minBalance = self.getMinimumBalance()
        if initialBalance < minBalance:
            raise ValueError(
                f"{self.getAccountType()} account requires minimum balance of ₹{float(minBalance)}. Provided: ₹{float(initialBalance)}"
            )

        # Initialize all fields
        self.accountNumber = accountNumber
        self.name = name
        self.age = age
        self.balance = float(initialBalance)
        self.status = "Active"
        self.pin = None

    # ===== Business Methods =====
    def deposit(self, amount):
        self.validateActive()
        if amount <= 0:
            raise InvalidAmountException(
                f"Deposit amount must be positive. Provided: ₹{float(amount)}"
            )
        self.balance += amount

    def withdraw(self, amount, pin):
        self.validateActive()
        self.validatePin(pin)
        self.validateAmount(amount)

        if amount > self.balance:
            raise InsufficientBalanceException(
                f"Insufficient balance. Available: ₹{float(self.balance)}, Requested: ₹{float(amount)}"
            )

        available_after = self.balance - amount
        if available_after < self.getMinimumBalance():
            raise MinimumBalanceViolationException(
                f"Cannot withdraw. Minimum balance of ₹{float(self.getMinimumBalance())} required. Available after withdrawal: ₹{float(available_after)}"
            )

        self.balance -= amount

    # ===== Account Status Management =====
    def closeAccount(self):
        if self.status == "Inactive":
            raise RuntimeError("Account is already closed")
        self.status = "Inactive"

    def reopenAccount(self):
        if self.status == "Active":
            raise RuntimeError("Account is already active")
        self.status = "Active"

    # ===== PIN Management =====
    def setPin(self, pin):
        if pin is None or not isinstance(pin, int) or pin < self.MIN_PIN or pin > self.MAX_PIN:
            raise ValueError(
                f"PIN must be a 4-digit number ({self.MIN_PIN}-{self.MAX_PIN})"
            )
        self.pin = pin

    def verifyPin(self, pin):
        if self.pin is None:
            return False
        return self.pin == pin

    def hasPin(self):
        return self.pin is not None

    def validatePin(self, pin):
        if self.pin is None:
            raise InvalidPinException("PIN not set for this account")
        if self.pin != pin:
            raise InvalidPinException("Incorrect PIN")

    def validateAmount(self, amount):
        if amount <= 0:
            raise InvalidAmountException(
                f"Amount must be positive. Provided: ₹{float(amount)}"
            )

    # ===== Helper Methods =====
    def validateActive(self):
        if self.status != "Active":
            raise InactiveAccountException(
                "Account is inactive. Please reopen the account or contact support."
            )

    def updateDailyWithdrawalTotal(self, amount):
        pass

    # ===== Getters & Setters =====
    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        if age < self.MIN_AGE:
            raise ValueError(
                f"Customer must be at least {self.MIN_AGE} years old. Provided: {age}"
            )
        self.age = age

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = float(balance)

    def getStatus(self):
        return self.status

    def getPin(self):
        return self.pin

    def __str__(self):
        pin_str = "Yes" if self.hasPin() else "No"
        return f"Account #{self.accountNumber} | {self.name} ({self.age} yrs) | {self.getAccountType()} | ₹{float(self.balance)} | {self.status} | PIN: {pin_str}"
