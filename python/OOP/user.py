class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name} has a current balance of: {self.account_balance}")

def transfer_money(transfer_from, transfer_to, amount):
    transfer_from.account_balance -= amount
    transfer_to.account_balance += amount
    return transfer_from, transfer_to


wacko = User("wacko", "wacko@animaniacs.com")
yacko = User("yacko", "yacko@animaniacs.com")
dot = User("dot", "dot@animaniacs.com")

wacko.make_deposit(43)
wacko.make_deposit(55)
wacko.make_deposit(4.61)
wacko.make_withdrawal(6.34)
wacko.display_user_balance()

yacko.make_deposit(73)
yacko.make_deposit(37.34)
yacko.make_withdrawal(6.34)
yacko.make_withdrawal(63.48)
yacko.display_user_balance()

dot.make_deposit(87.19)
dot.make_withdrawal(6.34)
dot.make_withdrawal(23.48)
dot.make_withdrawal(19.23)
dot.display_user_balance() #OUTPUT: "dot has a current balance of: 38.139999999999986" --> why is this not just 2 decimals?

wacko,dot=transfer_money(wacko,dot, 10.43)
wacko.display_user_balance()
dot.display_user_balance()