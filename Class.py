class Class:

    def __init__(self, name, first, second, third, fourth):
        self.name = name
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

    def getName(self):
        return self.name
    
    def getFirst (self):
        return self.first
    
    def getSecond(self):
        return self.second
    
    def getThird(self):
        return self.third
    
    def getFourth (self):
        return self.fourth

    def toString(self):
        return f'Name: {self.name} | First: {self.first} | Second: {self.second} | Third: {self.third} | Fourth: {self.fourth}'