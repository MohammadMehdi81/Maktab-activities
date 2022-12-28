from random import randint
import Bank
import User

def Register_Account():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    age = input("Enter your age: ")
    assert age.isdigit(), "invalid age!!!"
    bank = input("Enter your bank: ")
    assert bank == 'Tegarat' and bank == 'Saderat', 'invalid bank name!!!'
    new_acc = User.Account(fname.replace(" ",""), lname.replace(" ",""), age.replace(" ",""))
    if not new_acc.Check_Account_repeat():
        new_acc.Register()
        input("Account created!!!")
    else:
        print("This Account exist!!!")


def Menu():
    menu_items = [
        'Register Account',
        'Transaction',
        'Search Account',
        'about',
        'exit',
    ]

    line = "-" * 22

    while True:
        print("\n\n-------- Menu --------")

        for index, value in enumerate(menu_items):
            print(index + 1, value)
        print(line)

        try:
            user_number = int(input("> "))
            if user_number == 5:
                print("Bye!")
                break
            func = menu_items[user_number - 1]
            func = func.replace(" ", "_")

            eval(f"{func}()")

        # except (ValueError, IndexError):
        #     input("Error !!! \ninvalid key! \n\nPress enter to back main ... ")

        except AssertionError as msg:
            input(msg)
            eval(f"{func}()")
