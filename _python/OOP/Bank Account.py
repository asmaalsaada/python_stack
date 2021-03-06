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
            self.account_balance *= int_rate
        return self

acc1=bankAccount()
acc1.deposite(500).deposite(100).deposite(100).withdrawal(300).display_account_info()
acc2=bankAccount()
acc2.deposite(200).deposite(200).withdrawal(100).withdrawal(150).withdrawal(200).withdrawal(50).display_account_info()