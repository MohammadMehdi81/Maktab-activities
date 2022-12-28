from random import randint
import Bank

class Account:
    def __init__(self, fname, lname, age, bank):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.bank = bank

    def getname(self):
        return self.fname + " " + self.lname

    def getbank(self):
        return self.bank

    def getage(self):
        return self.age

    def Register(self):
        with open('Account.txt', 'a+') as f:
            f.write(f'{self.getname()}:{self.getage()}\n')

    def Check_Account_repeat(self):
        exist = False
        with open('Account.txt') as f:
            while True:
                line = f.readline()
                line = line.replace(" ", "")
                line = line.replace("\n", "")
                if not line:
                    break
                lines = line.split(":")
                if (lines[1] == self.age) and (lines[0] == (self.fname + self.lname)):
                    print('hi')
                    exist = True
        return exist


class Profile:
    def __init__(self, fname, lname, age, BankAccount):
        self.Account = Account(fname, lname, age)
        self.BankAccount = BankAccount




