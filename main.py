class Point:
    def __init__(self, name=None):
        if not isinstance(name, str):
            raise TypeError('Неверное имя')
        self.__name = name
    

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new):
        if not isinstance(new, str):
            raise TypeError('Неверное имя')
        self.__name = new


p = Point('Ильяс')
print(p.name)