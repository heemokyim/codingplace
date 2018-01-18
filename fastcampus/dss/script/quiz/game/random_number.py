import random
answer = random.randint(1,100)

count = 1

print(answer)

while True:
    guess = int(input("insert number : "))
    
    if answer == guess:
        break
    
    elif answer > guess:
        print('Up')
        
    elif answer < guess:
        print('Down')
    
    count+=1

print(count)