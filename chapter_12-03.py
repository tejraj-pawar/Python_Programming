'''
ATM Machine:
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

accounts = []
for i in range(0, 10):
    accounts.append(Account(i, 100))

while True:
    accId = eval(input('Enter an account id: '))
    if accId not in range(0, 10):
        continue

    account = accounts[accId]

    while True:
        menu = eval(input('Main menu \n 1: check balance \n 2: withdraw \n 3: deposit \n 4:exit \n'))

        if menu == 1:
            print('Balance is {}'.format(account.getBalance()))
        elif menu == 2:
            amount = eval(input('Enter amount to withdraw: '))
            account.withdraw(amount)
        elif menu == 3:
            amount = eval(input('Enter amount to deposit: '))
            account.deposit(amount)
        elif menu == 4:
            break
