import sys 
def print_lol(arg,indent=False,level=1,file=sys.stdout):
        for num in arg:
                if isinstance(num,list):
                        print_lol(num,indent,level+1,file)
                else:
                        if indent:
                                for tab in range(level):
                                        print('\t',end='',file=file)
                        print(num,file=file)

cast=[1234,3434,['qwer',[543,['how']]]]
