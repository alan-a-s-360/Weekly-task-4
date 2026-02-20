class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: ${amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    def display_balance(self):
        print("----- Account Details -----")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")
        print("---------------------------")
account1 = BankAccount("John Doe", "123456789", 1000)
account1.display_balance()
account1.deposit(500)
account1.withdraw(300)
account1.display_balance()                                                                                                                                                                                                                      Q1                                                                                                                                                                                                                 Q1
