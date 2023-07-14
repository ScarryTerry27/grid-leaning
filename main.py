class Point:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, name=None):
        if not isinstance(name, str):
            raise TypeError('Неверное имя')
        self.__name = name
    

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new):
        print(new)
        if not isinstance(new, str):
            raise TypeError('Неверное имя')
        self.__name = new


p = Point('Ильяс')
print(p.name)