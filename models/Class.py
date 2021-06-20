class Class:

    def __init__(self, name, first, second, third, fourth):
        self.name = name
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

    def toString(self):
        return f'Name: {self.name} | First: {self.first} | Second: {self.second} | Third: {self.third} | Fourth: {self.fourth}'