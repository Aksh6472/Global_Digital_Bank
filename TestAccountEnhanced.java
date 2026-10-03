public class TestAccountEnhanced {

    public static void main(String[] args) {

        System.out.println("============================================================");
        System.out.println("          ENHANCED ACCOUNT TEST (BOOLEAN RETURNS)");
        System.out.println("============================================================");

        // Test 1: Valid Account Creation
        System.out.println("\n>>> Test 1: Valid Account Creation");

        AccountEnhanced account1 = new AccountEnhanced(
                "1001", "John Doe", 25, 1000.0, "Savings"
        );

        displayAccount(account1);

        // Test 2: Invalid Age
        System.out.println("\n>>> Test 2: Invalid Age");

        System.out.println("Creating account with age 16");

        AccountEnhanced account2 = new AccountEnhanced(
                "1002", "Young Kid", 16, 500.0, "Savings"
        );

        System.out.println("Age auto-corrected to: " + account2.getAge());
        displayAccount(account2);

        // Test 3: Invalid Account Type
        System.out.println("\n>>> Test 3: Invalid Account Type");

        System.out.println("Creating account with type \"Invalid\"");

        AccountEnhanced account3 = new AccountEnhanced(
                "1003", "Test User", 25, 500.0, "Invalid"
        );

        System.out.println("Account type defaulted to: "
                + account3.getAccountType());

        displayAccount(account3);

        // Test 4: Minimum Balance on Creation
        System.out.println("\n>>> Test 4: Minimum Balance Enforcement");

        System.out.println("Creating Savings account with ₹300");

        AccountEnhanced account4 = new AccountEnhanced(
                "1004", "Bob Wilson", 25, 300.0, "Savings"
        );

        System.out.println("Balance auto-corrected to: ₹"
                + account4.getBalance());

        displayAccount(account4);

        // Test 5: Withdrawal Minimum Balance
        System.out.println("\n>>> Test 5: Withdrawal Minimum Balance");

        AccountEnhanced account5 = new AccountEnhanced(
                "1005", "Alice Brown", 30, 2000.0, "Current"
        );

        account5.setPin(1234);

        System.out.println("Initial:");
        displayAccount(account5);

        if (account5.withdraw(200.0, 1234)) {
            System.out.println("Withdrawing ₹200.0: SUCCESS");
        } else {
            System.out.println("Withdrawing ₹200.0: FAILED");
        }

        System.out.println("New balance: ₹" + account5.getBalance());

        if (account5.withdraw(900.0, 1234)) {
            System.out.println("Withdrawing ₹900.0: SUCCESS");
        } else {
            System.out.println(
                    "Withdrawing ₹900.0: FAILED (Minimum balance violation)"
            );
        }

        System.out.println("Current balance: ₹" + account5.getBalance());

        // Test 6: Account Status Management
        System.out.println("\n>>> Test 6: Account Status Management");

        AccountEnhanced account6 = new AccountEnhanced(
                "1006", "Charlie Green", 35, 2000.0, "Savings"
        );

        System.out.println("Initial:");
        displayAccount(account6);

        if (account6.closeAccount()) {
            System.out.println("Closing account: SUCCESS");
        } else {
            System.out.println("Closing account: FAILED");
        }

        System.out.println("After close:");
        displayAccount(account6);

        if (account6.deposit(500.0)) {
            System.out.println("Depositing ₹500.0: SUCCESS");
        } else {
            System.out.println(
                    "Depositing ₹500.0: FAILED (Account inactive)"
            );
        }

        if (account6.reopenAccount()) {
            System.out.println("Reopening account: SUCCESS");
        } else {
            System.out.println("Reopening account: FAILED");
        }

        System.out.println("After reopen:");
        displayAccount(account6);

        // Test 7: PIN Protection
        System.out.println("\n>>> Test 7: PIN Protection");

        AccountEnhanced account7 = new AccountEnhanced(
                "1007", "Diana Prince", 28, 1500.0, "Savings"
        );

        if (account7.setPin(1234)) {
            System.out.println("Setting PIN 1234: SUCCESS");
        } else {
            System.out.println("Setting PIN 1234: FAILED");
        }

        if (account7.verifyPin(1234)) {
            System.out.println("Verifying correct PIN: SUCCESS");
        } else {
            System.out.println("Verifying correct PIN: FAILED");
        }

        if (account7.verifyPin(9999)) {
            System.out.println("Verifying incorrect PIN: SUCCESS");
        } else {
            System.out.println("Verifying incorrect PIN: FAILED");
        }

        if (account7.withdraw(200.0, 1234)) {
            System.out.println("Withdrawing ₹200.0 with correct PIN: SUCCESS");
        } else {
            System.out.println("Withdrawing ₹200.0 with correct PIN: FAILED");
        }

        System.out.println("New balance: ₹" + account7.getBalance());

        if (account7.withdraw(100.0, 9999)) {
            System.out.println("Withdrawing ₹100.0 with incorrect PIN: SUCCESS");
        } else {
            System.out.println("Withdrawing ₹100.0 with incorrect PIN: FAILED");
        }

        // Test withdrawal when PIN is not set
        AccountEnhanced account8 = new AccountEnhanced(
                "1008", "No PIN User", 25, 1000.0, "Savings"
        );

        if (account8.withdraw(100.0, 1234)) {
            System.out.println("Withdrawal without PIN set: SUCCESS");
        } else {
            System.out.println("Withdrawal without PIN set: FAILED");
        }

        // Test 8: All Accounts Summary
        System.out.println("\n>>> Test 8: All Accounts Summary");

        displayAccount(account1);
        displayAccount(account2);
        displayAccount(account3);
        displayAccount(account4);
        displayAccount(account5);
        displayAccount(account6);
        displayAccount(account7);
        displayAccount(account8);

        System.out.println("\n============================================================");
        System.out.println("              ENHANCED TEST COMPLETED!");
        System.out.println("============================================================");
    }

    // Display formatting is handled only in the test class
    public static void displayAccount(AccountEnhanced account) {

        String pinStatus;

        if (account.hasPin()) {
            pinStatus = "Yes";
        } else {
            pinStatus = "No";
        }

        System.out.println(
                "Account #" + account.getAccountNumber()
                + " | " + account.getName()
                + " (" + account.getAge() + " yrs)"
                + " | " + account.getAccountType()
                + " | ₹" + account.getBalance()
                + " | " + account.getStatus()
                + " | PIN: " + pinStatus
        );
    }
}