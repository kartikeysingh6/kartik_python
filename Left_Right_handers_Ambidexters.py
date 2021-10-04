a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
if a>b :
    y=b+c
    if y>a :
        if (c-a+b)%2==0 :
            print(a*2+((c-a+b)))
        else :
            print(a*2+((c-a+b-1)))
    else :
        print(y*2)
elif b>a :
    y=a+c
    if y>b :
        if (c-b+a)%2==0 :
           print(b*2+((c-b+a)))
        else :
           print(b*2+((c-b+a-1)))
    else :
        print(y*2)
if a==b  :
    j=a+b+c
    if j%2==0 :
        print(j)
    else :
         print(j-1)
