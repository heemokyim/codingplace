class simple:
    pre="You said "
    post='\n'+'-'*20+'\n'

    def __init__(self):
        print('call init !'+self.post)

    def print_fix(self,string):
        print(self.pre +string+ self.post)

s1 = simple()
s1.print_fix("I'm dope !")
