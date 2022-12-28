
def check(equation):
    list1 = equation.split(" ")
    if len(list1)!= 3:
        raise InvalidNormalException()

    if list1[0].isdigit() or list1[2].isdigit():
        raise InvalidNumberException()

    if list1[1] not in ['+', '-', '*', '/']:
        raise InvalidOperaorException()

def InvalidNormalException():
    print("Your input desnt has valid form!!")

def InvalidNumberException():
    print("Your first or third number is not digit!!")

def InvalidOperaorException():
    print("Your operation is not valid!!")

