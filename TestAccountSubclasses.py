from Account import Account
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
from exceptions import (
    AccountException,
    InvalidAmountException,
    InsufficientBalanceException,
    MinimumBalanceViolationException,
    InactiveAccountException,
    InvalidPinException,
)

class TestAccountSubclasses:
    @staticmethod
    def run_tests():
        print("============================================================")
        print(" ACCOUNT SUBCLASSES TEST (SAVINGS & CURRENT)")
        print("============================================================")

        all_accounts = []

        # >>> Test 1: Creating Accounts
        print(">>> Test 1: Creating Accounts")
        account1 = SavingsAccount("1001", "John Doe", 25, 1000.0)
        account2 = CurrentAccount("1002", "Jane Smith", 30, 2000.0)
        all_accounts.append(account1)
        all_accounts.append(account2)
        print(f"Savings Account: {account1}")
        print(f"Current Account: {account2}")

        # >>> Test 2: Account Type and Minimum Balance
        print(">>> Test 2: Account Type and Minimum Balance")
        print(f"Savings Account - Type: {account1.getAccountType()}, Minimum Balance: ₹{float(account1.getMinimumBalance())}")
        print(f"Current Account - Type: {account2.getAccountType()}, Minimum Balance: ₹{float(account2.getMinimumBalance())}")

        # >>> Test 3: Savings Account - Interest Calculation
        print(">>> Test 3: Savings Account - Interest Calculation")
        print(f"Savings Account: Account #{account1.getAccountNumber()} | {account1.getName()} ({account1.getAge()} yrs) | {account1.getAccountType()} | ₹{float(account1.getBalance())} | {account1.getStatus()}\n")
        print(f"Interest Rate: {account1.getInterestRate()}% per annum")
        print(f"Interest for 1 year: ₹{account1.calculateInterest(1)}")
        print(f"Interest for 2 years: ₹{account1.calculateInterest(2)}")
        print(f"Interest for 5 years: ₹{account1.calculateInterest(5)}")
        balance_after_2_years = account1.getBalance() + account1.calculateInterest(2)
        print(f"After 2 years with interest: Balance would be ₹{balance_after_2_years}")

        # >>> Test 4: Current Account - Overdraft Feature
        print(">>> Test 4: Current Account - Overdraft Feature\n\n")
        print(f"Current Account: Account #{account2.getAccountNumber()} | {account2.getName()} ({account2.getAge()} yrs) | {account2.getAccountType()} | ₹{float(account2.getBalance())} | {account2.getStatus()}")
        print(f"Overdraft Limit: ₹{float(account2.getOverdraftLimit())}")
        print(f"Available Overdraft: ₹{float(account2.getAvailableOverdraft())}")
        print(f"Overdraft Used: ₹{float(account2.getOverdraftUsed())}")
        print(f"Is Using Overdraft: {str(account2.isUsingOverdraft()).lower()}")
        print("Withdrawing ₹1500.0 (goes below minimum balance of ₹1000)")
        print(f"Balance before: ₹{float(account2.getBalance())}")
        account2.setPin(1234)
        account2.withdraw(1500.0, 1234)
        print("Withdrawing: ₹1500.0 - SUCCESS")
        print(f"Balance after: ₹{float(account2.getBalance())}")
        print(f"Overdraft Used: ₹{float(account2.getOverdraftUsed())}")
        print(f"Available Overdraft: ₹{float(account2.getAvailableOverdraft())}")
        print(f"Is Using Overdraft: {str(account2.isUsingOverdraft()).lower()}")

        print("Attempting to withdraw ₹4000.0 (would exceed overdraft)")
        print(f"Available funds: ₹{float(account2.getBalance())} (balance) + ₹{float(account2.getAvailableOverdraft())} (overdraft) = ₹{float(account2.getBalance() + account2.getAvailableOverdraft())}")
        try:
            account2.withdraw(4000.0, 1234)
        except Exception as e:
            print(f"EXCEPTION: {e}")

        print("Repaying overdraft of ₹500.0")
        print(f"Balance before repayment: ₹{float(account2.getBalance())}")
        print(f"Overdraft Used before: ₹{float(account2.getOverdraftUsed())}")
        account2.repayOverdraft(500.0)
        print("Repaying ₹500.0 - SUCCESS")
        print(f"Balance after repayment: ₹{float(account2.getBalance())}")
        print(f"Overdraft Used after: ₹{float(account2.getOverdraftUsed())}")
        print(f"Is Using Overdraft: {str(account2.isUsingOverdraft()).lower()}")

        # >>> Test 5: Polymorphism - Treating Accounts Uniformly
        print(">>> Test 5: Polymorphism - Treating Accounts Uniformly")
        account3 = SavingsAccount("1003", "Bob Wilson", 35, 500.0)
        account4 = CurrentAccount("1004", "Alice Brown", 28, 1500.0)
        all_accounts.append(account3)
        all_accounts.append(account4)

        poly_accounts = [account1, account2, account3, account4]
        print("Processing accounts polymorphically:")
        total_balance = 0.0
        for acc in poly_accounts:
            print(f"Account #{acc.getAccountNumber()} | {acc.getName()} ({acc.getAge()} yrs) | {acc.getAccountType()} | ₹{float(acc.getBalance())} | {acc.getStatus()} | Type: {acc.getAccountType()}, Min Balance: ₹{float(acc.getMinimumBalance())}")
            total_balance += acc.getBalance()
        print(f"Total accounts: {len(poly_accounts)}")
        print(f"Total balance across all accounts: ₹{float(total_balance)}")

        # >>> Test 6: Validation - Invalid Creation Attempts
        print(">>> Test 6: Validation - Invalid Creation Attempts")
        print("Attempting to create SavingsAccount with ₹300 (below minimum)")
        try:
            SavingsAccount("9991", "Test Savings", 25, 300.0)
        except Exception as e:
            print(f"EXCEPTION: {e}")

        print("Attempting to create CurrentAccount with ₹500 (below minimum)")
        try:
            CurrentAccount("9992", "Test Current", 25, 500.0)
        except Exception as e:
            print(f"EXCEPTION: {e}")

        print("Attempting to create SavingsAccount with age 16")
        try:
            SavingsAccount("9993", "Test Age", 16, 1000.0)
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 7: Savings Account - PIN and Operations
        print(">>> Test 7: Savings Account - PIN and Operations")
        account5 = SavingsAccount("1005", "Charlie Green", 40, 2000.0)
        all_accounts.append(account5)
        print(f"Savings Account: Account #{account5.getAccountNumber()} | {account5.getName()} ({account5.getAge()} yrs) | {account5.getAccountType()} | ₹{float(account5.getBalance())} | {account5.getStatus()}")
        account5.setPin(1234)
        print("Setting PIN 1234: SUCCESS")
        account5.deposit(500.0)
        print("Depositing ₹500.0: SUCCESS")
        print(f"Balance after deposit: ₹{float(account5.getBalance())}")
        account5.withdraw(300.0, 1234)
        print("Withdrawing ₹300.0 with correct PIN: SUCCESS")
        print(f"Balance after withdrawal: ₹{float(account5.getBalance())}")
        print("Attempting to withdraw ₹2000.0 (would violate minimum balance)")
        try:
            account5.withdraw(2000.0, 1234)
        except Exception as e:
            print(f"EXCEPTION: {e}")

        # >>> Test 8: Current Account - Active Status Operations
        print(">>> Test 8: Current Account - Active Status Operations")
        account6 = CurrentAccount("1006", "Diana Prince", 35, 3000.0)
        all_accounts.append(account6)
        print(f"Current Account: Account #{account6.getAccountNumber()} | {account6.getName()} ({account6.getAge()} yrs) | {account6.getAccountType()} | ₹{float(account6.getBalance())} | {account6.getStatus()}")
        account6.closeAccount()
        print("Closing account: SUCCESS")
        print("Attempting to deposit ₹100.0 on closed account")
        try:
            account6.deposit(100.0)
        except Exception as e:
            print(f"EXCEPTION: {e}")
        account6.reopenAccount()
        print("Reopening account: SUCCESS")
        account6.deposit(100.0)
        print("Depositing ₹100.0 after reopen: SUCCESS")
        print(f"Balance after deposit: ₹{float(account6.getBalance())}")

        # >>> Test 9: All Accounts Summary
        print(">>> Test 9: All Accounts Summary")
        account2.pin = None
        for acc in all_accounts:
            print(acc)

        print("============================================================")
        print(" TEST COMPLETED!")
        print("============================================================")

if __name__ == "__main__":
    TestAccountSubclasses.run_tests()
