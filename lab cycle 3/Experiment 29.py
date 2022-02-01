class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
    
    def accountdetails(self):
        ac_num = input("Enter account number:")
        name = input("Enter name of the account holder:")
        type = input("Enter type of account:")
        self.name = name
        self.ac_num = ac_num
        self.type = type
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance  ")
 
    def display(self):
        print("\nACCOUNT DETAILS")
        print("Account Number:",self.ac_num)
        print("Name of the Account Holder:",self.name)
        print("Account Type:",self.type)
        print("Net Available Balance:",self.balance)
 
s = Bank_Account()
s.accountdetails()
s.deposit()
s.withdraw()
s.display()