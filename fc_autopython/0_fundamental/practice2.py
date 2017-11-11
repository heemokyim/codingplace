list_var = [i for i in range(9)]
str_var = 'woongley'
tuple_var = (i for i in range(3))
dict_var = {'name':'Jaewoong Lee'}

# print(len(list_var))
# print(len(dict_var))
# print(tuple_var)

for idx,val in enumerate(list_var):
    print(idx,val)

for idx in range(len(list_var)):
    print(idx,list_var[idx])

print('-'*10)
print(list(range(10)))

user_input = input('INSERT YOUR INPUT : ')
print(user_input)
