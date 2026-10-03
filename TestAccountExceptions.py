from Account import Account
from exceptions import (
    AccountException,
    InvalidAmountException,
    InsufficientBalanceException,
    MinimumBalanceViolationException,
    InactiveAccountException,
    InvalidPinException,
)

class TestAccountExceptions:
    @staticmethod
    def run_tests():
        print("============================================================")
        print(" ACCOUNT TEST WITH EXCEPTIONS")
        print("============================================================")

        accounts = []

        # >>> Test 1: Valid Account Creation
        print(">>> Test 1: Valid Account Creation")
        try:
            account1 = Account("1001", "John Doe", 25, 1000.0, "Savings")
            accounts.append(account1)
            print(f"SUCCESS: {account1}")
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 2: Invalid Age (under 18)
        print(">>> Test 2: Invalid Age (under 18)")
        try:
            account2 = Account("1002", "Young Kid", 16, 500.0, "Savings")
            accounts.append(account2)
            print(f"SUCCESS: {account2}")
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 3: Invalid Account Type
        print(">>> Test 3: Invalid Account Type")
        try:
            account3 = Account("1003", "Test User", 25, 500.0, "Invalid")
            accounts.append(account3)
            print(f"SUCCESS: {account3}")
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 4: Minimum Balance on Creation
        print(">>> Test 4: Minimum Balance on Creation\n")
        print("Creating Savings account with ₹300\n\n")
        try:
            account4 = Account("1004", "Bob Wilson", 25, 300.0, "Savings")
            accounts.append(account4)
            print(f"SUCCESS: {account4}")
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 5: Valid Deposit and Withdrawal
        print(">>> Test 5: Valid Deposit and Withdrawal")
        try:
            account5 = Account("1005", "Alice Brown", 30, 1000.0, "Current")
            accounts.append(account5)
            print(f"Account: {account5}")
            account5.setPin(1234)
            print("Setting PIN 1234: SUCCESS")
            account5.deposit(500.0)
            print("Depositing ₹500.0: SUCCESS")
            print(f"Balance after deposit: ₹{account5.getBalance()}")
            account5.withdraw(200.0, 1234)
            print("Withdrawing ₹200.0: SUCCESS")
            print(f"Balance after withdrawal: ₹{account5.getBalance()}")
            print(account5)
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 6: Invalid Deposit (Negative Amount)
        print(">>> Test 6: Invalid Deposit (Negative Amount)")
        try:
            print("Attempting to deposit ₹-100.0")
            account5.deposit(-100.0)
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 7: Insufficient Balance
        print(">>> Test 7: Insufficient Balance")
        try:
            account6 = Account("1006", "Charlie Green", 35, 500.0, "Savings")
            account6.setPin(1234)
            accounts.append(account6)
            print(f"Account: {account6}")
            print("Attempting to withdraw ₹1000.0")
            account6.withdraw(1000.0, 1234)
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 8: Minimum Balance Violation
        print(">>> Test 8: Minimum Balance Violation")
        try:
            account7 = Account("1007", "Diana Prince", 28, 1000.0, "Savings")
            account7.setPin(1234)
            accounts.append(account7)
            print(f"Account: {account7}")
            print("Attempting to withdraw ₹600.0")
            account7.withdraw(600.0, 1234)
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 9: Inactive Account Operations
        print(">>> Test 9: Inactive Account Operations")
        try:
            account8 = Account("1008", "Eve Wilson", 32, 2000.0, "Current")
            accounts.append(account8)
            print(f"Account: {account8}")
            account8.closeAccount()
            print("Closing account: SUCCESS")
            print("Attempting to deposit ₹100.0 on closed account")
            try:
                account8.deposit(100.0)
            except Exception as e:
                print(f"EXCEPTION: {e}")
            account8.reopenAccount()
            print("Reopening account: SUCCESS")
            account8.deposit(100.0)
            print("Depositing ₹100.0 after reopen: SUCCESS")
            print(f"Balance after deposit: ₹{account8.getBalance()}")
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 10: PIN Verification
        print(">>> Test 10: PIN Verification")
        try:
            account9 = Account("1009", "Frank Miller", 40, 1500.0, "Savings")
            accounts.append(account9)
            print(f"Account: {account9}")
            account9.setPin(1234)
            print("Setting PIN 1234: SUCCESS")
            account9.withdraw(200.0, 1234)
            print("Withdrawing ₹200.0 with correct PIN: SUCCESS")
            print(f"Balance: ₹{account9.getBalance()}")

            print("Attempting to withdraw ₹100.0 with incorrect PIN (9999)")
            try:
                account9.withdraw(100.0, 9999)
            except Exception as e:
                print(f"EXCEPTION: {e}")

            print("Attempting to withdraw ₹100.0 without PIN set")
            try:
                temp_account = Account("9999", "Temp No Pin", 25, 1000.0, "Savings")
                temp_account.withdraw(100.0, 1234)
            except Exception as e:
                print(f"EXCEPTION: {e}")
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 11: All Accounts Summary
        print(">>> Test 11: All Accounts Summary")
        for acc in accounts:
            print(acc)

        print("============================================================")
        print(" TEST COMPLETED!")
        print("============================================================")

if __name__ == "__main__":
    TestAccountExceptions.run_tests()
