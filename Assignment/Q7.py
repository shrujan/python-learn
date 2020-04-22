class BankAccount:
    
    def __init__(self, initalBalance):
        self.balance = initalBalance
        
    def showBalance(self):
        print('Your Account Balance is %s' % (self.balance))

    def deposit(self, amount):
        self.balance += amount
        print('Your Account Balance is %s' % (self.balance))


    def withdraw(self, amount):
        if amount > self.balance:
            print('Error ... You can withdraw less than ' + str(self.balance))
        else:
            self.balance -= amount
            print('Your Account Balance is %s' % (str(self.balance)))

user = BankAccount(60000)

user.showBalance()
user.deposit(int(input('Enter amount to deposit ')))

user.withdraw(int(input('Enter amount to withdraw ')))
