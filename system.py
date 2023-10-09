



class Account:
    def __init__(self, account_holder,  account_number, balance, account_status, account_type):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.account_holder = account_holder
        self.account_status = account_status
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return f"${self.balance}.00"
    
    def get_account_number(self):
        return self.account_number
    
    def get_account_type(self):
        return self.account_type
    
    def get_account_status(self):
        return self.account_status
    
    def get_account_details(self):
        return {
            "Account Name": self.account_holder,
            "Account Number": self.account_number,
            "Balance": self.balance,
            "Account Status": self.account_status,
            "Account Type": self.account_type
        }

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()

    def get_account_type(self):
        self.account_type = "Savings"
        return self.account_type

    def get_account_details(self):
        pass

class CurrentAccount(Account):
    def __init__(self):
        super().__init__()

    def get_account_type(self):
        self.account_type = "Current"
        return self.account_type

    def get_account_details(self):
        pass


user1 = Account("John Doe", "0244288437", 200, "Active", "Tier 3 Savings Account.")

# print(f"Account Name: {user1.account_holder}")
# print(f"Account Type: {user1.get_account_type()}")
# print(f"Account Number: {user1.account_number}")
# print(f"Balance: {user1.get_balance()}")
# user1.deposit(100)
# print(f"New Balance: {user1.get_balance()}")
print(user1.get_account_details())