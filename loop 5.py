s=0
n=int(input("enter a number"))
for i in range(1,n+1):
  for j in range (i,0,-1):
    s+=1
    print(s,end="")
  print()