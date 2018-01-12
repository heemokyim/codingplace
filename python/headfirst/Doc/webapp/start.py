﻿import pickle
from athletemodel import Athlete
from athletemodel import fileRead

file_list=['myapp\sarah2.txt','myapp\julie2.txt','myapp\mikey2.txt','myapp\james2.txt']
#file_list includes all file's name

def put_to_store(file_list):
    all_athletes=dict()
    for each in file_list:
        buf=fileRead(each)
        all_athletes[buf.name]=buf
    try:
        with open('data.pickle','wb') as fd:
            pickle.dump(all_athletes,fd)
    except IOError as ioerr:
        print("IOError has occured : "+str(ioerr))
        return None
    return all_athletes

def get_from_store():
    all_athletes=dict()
    try:
        with open('data.pickle','rb') as fd:
            all_athletes=pickle.load(fd)
    except IOError as ioerr:
        print("IOError has occured : "+str(ioerr))
        return None
    return all_athletes
