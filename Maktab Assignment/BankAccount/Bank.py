from random import randint

class BankAccount:
    def __init__(self, name):
        self.name = name


class SaderatAccount(BankAccount):
    def __init__(self, Account, balance):
        self.__balance = balance  # private -> priv8
        self.__key = randint(100, 999)  # protect
        self.Account = Account

    def get_balance(self):
        return self.__balance

    # def __repr__(self):
    #     return f"<{self.name.title()}: {self.__balance}>"

    def Register(self):
        with open('SaderatAccounts.txt', 'a+') as f:
            f.write(f'{self.Account.getname()}:{self.Account.getage()}:{self.__balance()}\n')


class TegaratAccount(BankAccount):
    def __init__(self, name, balance):
        self.__balance = balance  # private -> priv8
        self.__key = randint(100, 999)  # protect
        self.name = name

    def get_balance(self):
        return self.__balance

    # def __repr__(self):
    #     return f"<{self.name.title()}: {self.__balance}>"

    def Register(self):
        with open('TegaratAccounts.txt', 'a+') as f:
            f.write(f'{self.Account.getname()}:{self.Account.getage()}:{self.__balance()}\n')









