class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,dep_amt):
        self.balance+=dep_amt
        print(f"deposited amount is {dep_amt}")
    def with_drawal(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance-=wd_amt
            print(f"{wd_amt} amount is deducted from your account")
        else:
            print("Insufficent amount")
    def __str__(self):
        return f"Owner : {self.owner}\nBalance : {self.balance}"

a=Account("Sam",500)
a.owner
a.balance
a.deposit(400)
a.with_drawal(300)
print(a)