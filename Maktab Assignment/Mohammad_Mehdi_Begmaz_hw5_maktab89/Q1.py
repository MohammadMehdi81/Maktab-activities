class Singleton:
    __instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if Singleton.__instance:
            Singleton.__instance = super(Singleton, cls).__new__(cls)
        return Singleton.__instance


akbar = Singleton()
asghar = Singleton()
print(akbar == asghar)
print(id(akbar) == id(asghar))
