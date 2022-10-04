def is_Armstrong(n):
    sum = 0
    m = n
    while n != 0:
        b = n % 10
        sum = sum + b*b*b
        n = n // 10
        
    if sum == m:
        print(sum," Is a Armstrong number")
    else:
        print("It's not a Armstrong number")
    

a = int(input("Enter no to check that it's Armstrong or not :"))
is_Armstrong(a)
