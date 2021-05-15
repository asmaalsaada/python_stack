class bankAccount:
    def __init__(self ):
        self.int_rate = 0.01
        self.account_balance = 0

    def deposite(self, amount):
        self.account_balance += amount
        return self

    def withdrawal(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0 : 
            print("Insufficient funds: Charging a 5 USD fee") 
            self.account_balance -= 5
        return self

    def display_account_info(self):
        print(self.account_balance)
        return self
        
    def yield_interest(self):   
        if self.account_balance > 0 :
            self.account_balance *= self.int_rate
        return self
class user:
    def __init__(self,  name):
        self.name = name
        self.bankAccount = bankAccount()

    def make_deposite(self, amount):
        self.account_balance.deposite
    def make_withdrawal(self, amount):
        self.account_balance.withdrawal
    def display_user_balance(self):
        pass
User1 = user('dee')
User1.bankAccount.deposite(300)
print("User1 has account balance of {} . " .format(User1.bankAccount.display_account_info()))