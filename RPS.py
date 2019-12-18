import random
n=random.randint(1,3)
if n==1:
    c="rock"
elif n==2:
    c="paper"
else:
    c="scissor"
print("R. Rock\nP. Paper\nS. Scissor\n")
u=input("Enter your choice: ")
print("\n")
if u.lower()=="rock" or u.lower()=="r" or u.lower()=="a" or u=="1" :
    ur="rock"
    print("You choosed rock")
elif u.lower()=="paper" or u.lower()=="p" or u.lower()=="b" or u=="2" :
    ur="paper"
    print("You choosed paper")
elif u.lower()=="scissor" or u.lower()=="s" or u.lower()=="c" or u=="3" :
    ur="scissor"
    print("You choosed scissor")
else:
    print("Invalid Input!")

print("Computer choosed " + c)
print("\n")
if ur==c:
    print("It's DRAW!")
elif ur=="rock":
    if c=="paper":
        print("Computer Wins!")
    elif c=="scissor":
        print("You Win!")
elif ur=="paper":
    if c=="rock":
        print("You Win!")
    elif c=="scissor":
        print("Computer Wins!")
else:
    if c=="paper":
        print("You Win!")
    elif c=="rock":
        print("Computer Wins!")