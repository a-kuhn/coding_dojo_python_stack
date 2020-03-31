class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name} has a current balance of: {self.account_balance}")
        return self

def transfer_money(transfer_from, transfer_to, amount):
    transfer_from.account_balance -= amount
    transfer_to.account_balance += amount
    return transfer_from, transfer_to


wacko = User("wacko", "wacko@animaniacs.com")
yacko = User("yacko", "yacko@animaniacs.com")
dot = User("dot", "dot@animaniacs.com")

wacko.make_deposit(43).make_deposit(55).make_deposit(4.61).make_withdrawal(6.34).display_user_balance()

yacko.make_deposit(73).make_deposit(37.34).make_withdrawal(6.34).make_withdrawal(63.48).display_user_balance()

dot.make_deposit(87.19).make_withdrawal(6.34).make_withdrawal(23.48).make_withdrawal(19.23).display_user_balance() #OUTPUT: "dot has a current balance of: 38.139999999999986" --> why is this not just 2 decimals?

transfer_money(wacko, dot, 10.43)
wacko.display_user_balance()
dot.display_user_balance()