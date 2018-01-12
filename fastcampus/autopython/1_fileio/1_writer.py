# user_input = input()
# datafile = open('data/writed_file.txt','w')
# datafile.write(user_input+'\n')

user_input = input()
datafile = open('data/writed_file.txt','a')
datafile.write(user_input+'\n')
