class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        bank_acc = BankAccount(acct_name = name+"_acct1")
        self.accounts = {bank_acc.acct_name: bank_acc}
    
    def make_deposit(self, amount, account):
        self.accounts[account].deposit(amount)
    
    def make_withdrawal(self, amount, account):
        self.accounts[account].withdrawal(amount)

    def display_user_balance(self, account):
        print(f"{self.name} has a current balance of: {self.account.balance}")

    def new_acct(self, account_name, balance, int_rate=0.017):
        self.accounts[account_name] = BankAccount(account_name, balance, int_rate=0.017)


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

# make 3 user accounts
wacko = User("wacko", "wacko@animaniacs.com")
yacko = User("yacko", "yacko@animaniacs.com")
dot = User("dot", "dot@animaniacs.com")

#make initial deposit
wacko.make_deposit(1000, "wacko_acct1")

#create new account w. initial deposit
wacko.new_acct("wacko_acct2", 1500)

#check balance of both accounts
print("wacko_acct1 = ", wacko.accounts["wacko_acct1"].balance)
print("wacko_acct2 = ",wacko.accounts["wacko_acct2"].balance)

#same as above
yacko.make_deposit(2000, "yacko_acct1")
yacko.new_acct("yacko_acct2", 2500)
print("yacko_acct1 = ",yacko.accounts["yacko_acct1"].balance)
print("yacko_acct2 = ",yacko.accounts["yacko_acct2"].balance)

#same as above
dot.make_deposit(3000, "dot_acct1")
dot.new_acct("dot_acct2", 3500)
print("dot_acct1 = ",dot.accounts["dot_acct1"].balance)
print("dot_acct2 = ",dot.accounts["dot_acct2"].balance)

#test transfer_money() -->this also tests deposit() & withdrawal()
transfer_money(wacko, "wacko_acct1", dot, "dot_acct1", 10.43)
print("wacko_acct1: {}".format(wacko.accounts["wacko_acct1"].balance))
print("dot_acct1: {}".format(dot.accounts["dot_acct1"].balance))

