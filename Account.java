public class Account{
  /*accountNumber int Unique account number
name String Account holder's full name
age int Account holder's age
balance double Current account balance
accountType String Type of account ("Savings" or "Current")
status String Account status ("Active" or "Inactive") */
        private int accountNumber;
        private String name;
        private int age;
        private double balance;
        private String accountType;
        private String status;

        public Account(int accountNumber, String name, int age, double initialBalance, String accountType){
            this.accountNumber=accountNumber;
            this.name=name;
            this.age=age;
            //why intitialbalnce is because the pdf has stated Accepts: accountNumber, name, age, initialBalance, accountType
            this.balance=initialBalance;
            this.accountType=accountType;
            this.status="Active";

        }
        //deposit
        public boolean deposit(double amount){
            if(amount>0){
                balance+=amount;
                return true;
            }else{
                return false;
            }
        }
        //withdraw
        public boolean withdraw(double amount){
            if(amount>0 && amount<=balance){
                balance-=amount;
                return true;
            }else{
                return false;
            }
        }
        public int getAccountNumber() {
        return accountNumber;
        }
        public String getName() {
        return name;
        }
        public int getAge(){
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
        public void setName(String name){
        this.name=name;
        }
        public void setAge(int age){
            this.age=age;
        }
    }
