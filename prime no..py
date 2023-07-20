n=int(input("Enter a number "))
f=0
for i in range(2,int(n/2)+1):
  if n%i==0:
    print("Not a prime number")
    f=1
    break
if f==0:
  print("Prime number")    