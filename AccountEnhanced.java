public class AccountEnhanced {

    // Fields
    private String accountNumber;
    private String name;
    private int age;
    private double balance;
    private String accountType;
    private String status;
    private Integer pin;


    // Constructor
    public AccountEnhanced(String accountNumber, String name, int age,
                           double initialBalance, String accountType) {

        this.accountNumber = accountNumber;
        this.name = name;

        // Enhancement 1: Age validation
        if (age < 18) {
            this.age = 18;
        } else {
            this.age = age;
        }

        // Enhancement 2: Account type validation
        if (accountType.equals("Savings") || accountType.equals("Current")) {
            this.accountType = accountType;
        } else {
            this.accountType = "Savings";
        }

        // Enhancement 3: Minimum balance on creation
        if (this.accountType.equals("Savings")) {

            if (initialBalance < 500) {
                this.balance = 500;
            } else {
                this.balance = initialBalance;
            }

        } else if (this.accountType.equals("Current")) {

            if (initialBalance < 1000) {
                this.balance = 1000;
            } else {
                this.balance = initialBalance;
            }
        }

        // Default values
        this.status = "Active";
        this.pin = null;
    }


    // Deposit
    public boolean deposit(double amount) {

        // Check account status
        if (!status.equals("Active")) {
            return false;
        }

        if (amount <= 0) {
            return false;
        }

        balance += amount;
        return true;
    }


    // Withdraw with PIN
    public boolean withdraw(double amount, int pin) {

        // Check account status
        if (!status.equals("Active")) {
            return false;
        }

        // Check PIN
        if (!verifyPin(pin)) {
            return false;
        }

        // Check amount
        if (amount <= 0) {
            return false;
        }

        // Calculate balance after withdrawal
        double newBalance = balance - amount;

        // Minimum balance rule
        if (accountType.equals("Savings") && newBalance < 500) {
            return false;
        }

        if (accountType.equals("Current") && newBalance < 1000) {
            return false;
        }

        balance = newBalance;
        return true;
    }


    // Close account
    public boolean closeAccount() {

        if (status.equals("Inactive")) {
            return false;
        }

        status = "Inactive";
        return true;
    }


    // Reopen account
    public boolean reopenAccount() {

        if (status.equals("Active")) {
            return false;
        }

        status = "Active";
        return true;
    }


    // Set PIN
    public boolean setPin(int pin) {

        // PIN must be a 4-digit number
        if (pin >= 1000 && pin <= 9999) {
            this.pin = pin;
            return true;
        }

        return false;
    }


    // Verify PIN
    public boolean verifyPin(int pin) {

        // No PIN has been set
        if (this.pin == null) {
            return false;
        }

        // Check whether PIN matches
        return this.pin == pin;
    }


    // Check if PIN exists
    public boolean hasPin() {
        return pin != null;
    }


    // Getters
    public String getAccountNumber() {
        return accountNumber;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public double getBalance() {
        return balance;
    }

    public String getAccountType() {
        return accountType;
    }

    public String getStatus() {
        return status;
    }
}