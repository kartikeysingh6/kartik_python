output=""

n=30

if(n%3==0):
  output+="Fizz"
if(n%5==0):
  output+="Buzz"
if(output==""):
  output=str(n)
  
print(output)
