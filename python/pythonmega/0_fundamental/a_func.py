# age = input()

import sys

                    # default parameters
def minutes_to_hours(minutes=60,seconds=3600):
    return minutes/60 +seconds/3600

if __name__=="__main__":
    first=0
    second=0

    # setting arguments
    if 2<=len(sys.argv)<=3:
        first=int(sys.argv[1])
        second=int(sys.argv[2])

    # passing arguments
    print(minutes_to_hours(first,second))
