def func(v):
    i=v+3
    return i

class myclass:
    def __init__(self,a=1,b=2):
        self.a=a
        self.b=b

    def show(self):
        print(f'a={self.a},b={self.b},sum{self.sum()}')

    def sum(self):
        return self.a + self.b