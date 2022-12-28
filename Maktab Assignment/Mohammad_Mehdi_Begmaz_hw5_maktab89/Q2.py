class Add:
    def __init__(self, number = 0):
        self.number = number

    def add(self, value):
        self.number += value
        return self.number

    def __call__(self, *args, **kwargs):
        self.number = self.add(args[0])
        return self

    def __repr__(self):
        return str(self.number)


# without build object
print(Add(40)(2)(46))


# with build object
x = Add()
print(x(40)(2)(-34))


