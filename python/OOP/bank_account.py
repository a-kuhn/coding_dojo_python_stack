class BankAccount:
    def __init__(self, balance=0, int_rate=0.017):
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

acct1 = BankAccount(400,0.017)
acct2 = BankAccount(37,0.017)

acct2.display_account_info()

acct1.deposit(200).deposit(150).deposit(1000).withdrawal(650).yield_interest().display_account_info()

acct2.deposit(4000).deposit(130).withdrawal(400).withdrawal(1000).withdrawal(49).withdrawal(198).yield_interest().display_account_info()
