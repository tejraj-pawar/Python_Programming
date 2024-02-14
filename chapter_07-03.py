'''
(The Account class) Design a class named Account that contains:

'''

class Account:
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def setId(self, id):
        self.id = id

    def setBalance(self, balance):
        self.balance = balance

    def setAnnualInterestRate(self, annualInterestRate):
        self.annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.balance * (self.annualInterestRate / 12)

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

account = Account(1122, 20000, 4.5)
account.withdraw(2500)
account.deposit(3000)

print(account.getId(), account.getBalance(), account.getMonthlyInterestRate(), account.getMonthlyInterest())
