class simpleclass:
    def __init__(self, input):
        self.a = input

    def print_this(self):
        print(self.a)
        print('--'*20)

s1=simpleclass(1)
s2=simpleclass(2)

s1.print_this()
s2.print_this()

tmp=lambda x:x**2
print(tmp(2))
