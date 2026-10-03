public class TestAccount {

    public static void main(String[] args) {

        System.out.println("========================================");
        System.out.println("       GLOBAL DIGITAL BANK");
        System.out.println("         ACCOUNT TEST");
        System.out.println("========================================");

        // Create first account
        System.out.println("\n--- Creating Account 1 ---");

        Account account1 = new Account(
                1001,
                "John Doe",
                25,
                1000.0,
                "Savings"
        );

        System.out.println("Account created successfully!");
        displayAccount(account1);

        // Test deposit
        System.out.println("\n--- Testing Deposit ---");

        double depositAmount = 500.0;

        if (account1.deposit(depositAmount)) {
            System.out.println("Deposit of ₹" + depositAmount + " successful.");
        } else {
            System.out.println("Deposit failed: Invalid amount.");
        }

        System.out.println("Balance: ₹" + account1.getBalance());

        // Test invalid deposit
        depositAmount = -100.0;

        if (account1.deposit(depositAmount)) {
            System.out.println("Deposit of ₹" + depositAmount + " successful.");
        } else {
            System.out.println("Deposit failed: Invalid amount.");
        }

        // Test withdrawal
        System.out.println("\n--- Testing Withdrawal ---");

        double withdrawAmount = 200.0;

        if (account1.withdraw(withdrawAmount)) {
            System.out.println("Withdrawal of ₹" + withdrawAmount + " successful.");
        } else {
            System.out.println("Withdrawal failed.");
        }

        System.out.println("Balance: ₹" + account1.getBalance());

        // Test insufficient balance
        withdrawAmount = 2000.0;

        if (account1.withdraw(withdrawAmount)) {
            System.out.println("Withdrawal of ₹" + withdrawAmount + " successful.");
        } else {
            System.out.println("Withdrawal failed: Insufficient balance.");
        }

        // Create second account
        System.out.println("\n--- Creating Account 2 ---");

        Account account2 = new Account(
                1002,
                "Jane Smith",
                30,
                2000.0,
                "Current"
        );

        System.out.println("Account created successfully!");
        displayAccount(account2);

        // Display all accounts
        System.out.println("\n--- All Accounts ---");

        displayAccount(account1);
        displayAccount(account2);

        System.out.println("\n========================================");
        System.out.println("          TEST COMPLETED!");
        System.out.println("========================================");
    }

    // Displays account information
    public static void displayAccount(Account account) {

        System.out.println(
                "Account #" + account.getAccountNumber()
                + " | " + account.getName()
                + " (" + account.getAge() + " yrs)"
                + " | " + account.getAccountType()
                + " | ₹" + account.getBalance()
                + " | " + account.getStatus()
        );
    }
}