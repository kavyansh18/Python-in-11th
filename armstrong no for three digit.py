n=int(input("Enter a three digit number number "))
t=n
s=0
while n>0:
  s=s+(n%10)**3
  n=n//10
if s==t:
  print("Armstrong number")
else:
  print(" Not a Armstrong number")  