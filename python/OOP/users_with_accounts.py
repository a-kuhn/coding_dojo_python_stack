class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(acct_name = name+"_acct1")]
    
    def make_deposit(self, amount, account):
        for i in self.accounts:
            if i.acct_name == account:
                self.accounts[i].deposit(amount)
    
    def make_withdrawal(self, amount, account):
        self.account.deposit(amount)

    def display_user_balance(self, account):
        print(f"{self.name} has a current balance of: {self.account.balance}")

    def new_acct(self, account_name, balance=0, int_rate=0.017):
        self.accounts.append(BankAccount(account_name, balance, int_rate))


class BankAccount:
    def __init__(self, acct_name, balance=0, int_rate=0.017):
        self.acct_name = acct_name
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds. Charging $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"account balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1+self.int_rate)
        return self

def transfer_money(user1, user1_account, user2, user2_account, amount):
    user1.make_withdrawal(amount, user1_account)
    user2.make_deposit(amount, user2_account)
    return user1, user2


wacko = User("wacko", "wacko@animaniacs.com")
wacko.make_deposit(1000, "wacko_acct1")
print(wako.accounts[0].balance)

yacko = User("yacko", "yacko@animaniacs.com")
dot = User("dot", "dot@animaniacs.com")

# dot.make_deposit(3000, "dot_acct1")
wacko.make_deposit(1000, "wacko_acct1")
# yacko.make_deposit(2000, "yacko_acct1")

# dot.new_acct("dot_acct2", 3500)
# print(dot.accounts[0].balance)
# print(dot.accounts[1].balance)

# wacko.new_acct("wacko_acct2", 1500)
# print(wacko.accounts[0].balance)
# print(wacko.accounts[1].balance)

# yacko.new_acct("yacko_acct2", 2500)
# print(yacko.accounts[0].balance)
# print(yacko.accounts[1].balance)
# wacko,dot=transfer_money(wacko,wacko_acct1,dot,dot_acct1,10.43)
# wacko.display_user_balance(wacko_acct1)
# dot.display_user_balance(dot_acct1)