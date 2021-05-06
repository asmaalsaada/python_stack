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
print("User's name is {} and has {} balance".format(user1.name,user1.balance))

user2 = user("Asmaa")
user2.make_deposite(500)
user2.make_deposite(100)
user2.make_withdrawal(200)
user2.make_withdrawal(300)
print(user2.name)
print("User's name is {} and has {} balance".format(user2.name,user2.balance))

user3 = user("Denise")
user3.make_deposite(500)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.make_withdrawal(200)
print(user3.name)
print("User's name is {} and has {} balance".format(user3.name,user3.balance))