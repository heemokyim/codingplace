def age_foo(age):
    return float(age)+50

if __name__=="__main__":
    print(age_foo(input("Enter your age : ")))
elif __name__=="c_input":
    print('When import')

data=input('did you mean %s' % age_foo(50))
print(data)
