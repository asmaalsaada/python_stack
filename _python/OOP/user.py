class user:
    def __init__(self,  name):
        self.balance = 0
        self.name = name

    def make_deposite(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        pass


user1 = user("Qamar")
user1.make_deposite(500)
user1.make_deposite(100)
user1.make_deposite(200)
user1.make_withdrawal(300)
print(user1.name)
print("User's name is {} and has a {} balance".format(user1.name,user1.balance))

user1 = user("asmaa")
user1.make_deposite(500)
user1.make_deposite(100)
user1.make_withdrawal(200)
user1.make_withdrawal(300)
print(user1.name)
print("User's name is {} and has a {} balance".format(user1.name,user1.balance))

user1 = user("Qamar")
user1.make_deposite(500)
user1.make_withdrawal(100)
user1.make_withdrawal(100)
user1.make_withdrawal(200)
print(user1.name)
print("User's name is {} and has a {} balance".format(user1.name,user1.balance))