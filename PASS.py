import random

def rand_sym(num):
    a=random.randint(1,int(num))
    if a==1:
        return "~"
    elif a==2:
        return "`"
    elif a==3:
        return "!"
    elif a==4:
        return "@"
    elif a==5:
        return "#"
    elif a==6:
        return "$"
    elif a==7:
        return "%"
    elif a==8:
        return "^"
    elif a==9:
        return "&"
    elif a==10:
        return "*"
    elif a==11:
        return "+"
    elif a==12:
        return "-"
    elif a==13:
        return "/"
    else:
        return "#"

def rand_alfa(num):
    a=random.randint(1,int(num))
    if a==1:
        return "a"
    elif a==2:
        return "b"
    elif a==3:
        return "c"
    elif a==4:
        return "d"
    elif a==5:
        return "e"
    elif a==6:
        return "f"
    elif a==7:
        return "g"
    elif a==8:
        return "h"
    elif a==9:
        return "i"
    elif a==10:
        return "j"
    elif a==11:
        return "k"
    elif a==12:
        return "l"
    elif a==13:
        return "m"
    elif a==14:
        return "n"
    elif a==15:
        return "o"
    elif a==16:
        return "p"
    elif a==17:
        return "q"
    elif a==18:
        return "r"
    elif a==19:
        return "s"
    elif a==20:
        return "t"
    elif a==21:
        return "u"
    elif a==22:
        return "v"
    elif a==23:
        return "w"
    elif a==24:
        return "x"
    elif a==25:
        return "y"
    elif a==26:
        return "z"
    else:
        return "k"

#ln=int(input("Enter length of password: "))
al=int(input("Enter no. of alphabets: "))
nl=int(input("Enter no. of digits: "))
sl=int(input("Enter no. of symbols: "))
try:
    if al+nl+sl <=5 :
        print("Password should be atleast 6 characters long!")
    elif al+nl+sl >5 :
        print("\nRandomly Generated Password is: ")
        for length in range(al):
            print(rand_alfa(26))
        for length in range(nl):
            print(random.randint(0,9))
        for length in range(sl):
            print(rand_sym(13))
except ValueError:
    print("Invalid Input!")
