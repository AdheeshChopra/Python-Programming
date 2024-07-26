class Accounts:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited.")
        print("Total amount:", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited.")
        print("Total amount:", self.get_balance())

    # balance method
    def get_balance(self):
        return self.balance


acc1 = Accounts(100000, 12345)
acc1.debit(100)
acc1.credit(150000)
acc1.credit(50000)
acc1.debit(5000)