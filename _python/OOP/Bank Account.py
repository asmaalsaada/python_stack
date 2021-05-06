class bankAccount:
    def __init__(self ):
        self.int_rate = 0.01
        self.balance = 0

    def make_deposite(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        if self.balance < 0 : 
            print("Insufficient funds: Charging a 5 USD fee") 
            self.balance -= 5
        return self

    def display_account_info(self):
        print(self.balance)
        return self
        
    def yield_interest(self):   
        if self.balance > 0 :
            self.balance *= int_rate
        return self

acc1=bankAccount()
acc1.make_deposite(500).make_deposite(100).make_deposite(100).make_withdrawal(300).display_account_info()
acc2=bankAccount()
acc2.make_deposite(200).make_deposite(200).make_withdrawal(100).make_withdrawal(150).make_withdrawal(200).make_withdrawal(50).display_account_info()