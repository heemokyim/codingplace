# show users user-friendly message
# interactive dictionary
# 1. get word from user
# 2. return meaning of word
# 3. read data from json

# It is not efficient to put all data in memory and provide functions to users

# How about real time streaming?
# check data with stream mode (don't put all data in memory)
# return only matched data

import json
from difflib import SequenceMatcher as sm
from difflib import get_close_matches as gcm
# store all data as dictionary
data=json.load(open('data.json','r'))
data={key.lower():val for key,val in data.items()}

threshold=0.8

def translate(word):
    word=word.lower()

    if word in data.keys():
        return data[word]

    else:
        # 1. set threshold ratio
        # 2. If ratio exceed threshold, return it
        # 3. keep searching til meet threshold
        # Reason for setting threshold = too large to exhaustive-search
        # get_close_matches

        # max_sim, max_word = 0 , ""
        # result="Most similar word: "
        # for each in data.keys():
        #     sim_ratio=sm(None,word,each).ratio()
        #     if sim_ratio >= threshold:
        #         return result+each+"\n"+str(data[each])
        #     elif max_sim < sim_ratio:
        #         max_sim, max_word = sim_ratio, each
        # return result+max_word+"\n"+str(data[max_word])

        if len(gcm(word,data.keys(),cutoff=0.8))>0:
            return data[gcm(word,data.keys(),cutoff=0.8)[0]]
        else:
            return None



if __name__=="__main__":
    print(translate(input("Enter the word : ")))

## measure similarity between two string == difflib.SequenceMatcher

# from difflib import SequenceMatcher
# similar_ratio=SequenceMatcher(None,'rainNN','rain').ratio()

# from difflib import get_close_matches
# ex) get_close_matches("rain",["help","pyramid","rain"])
# >>> ['rain']