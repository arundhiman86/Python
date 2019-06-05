'''
Bank Account Problem

Create a bank account class that has two attributes:

* owner
* balance

and two methods:

* deposit
* withdraw

As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

'''

class Account():
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance}"

    def deposit(self, amt):
        self.balance = self.balance+amt
        return 'Deposite Accepted'
        
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return 'Withdrawl Accepted'
        else:
            return 'Funds Unavailable'
