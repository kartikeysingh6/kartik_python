import random
num=random.randint(0,20)
unum=-1
while(unum!=num):
    unum=int(input("\nEnter your guess: "))
    if num<unum:
        print("You gussed high!")
    elif num>unum:
        print("You gussed low!")
print("You guessed it!")