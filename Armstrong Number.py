n=input("Enter a number ")
s=0
for i in n:
  s=s+int(i)**len(n)
if s==int(n):
  print("Armstrong number")
else:
  print("Not an Armstrong number")    
