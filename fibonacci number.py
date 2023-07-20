n=int(input("Enter number of rows "))
f,s=0,1
i=3
if n<=0:
  print("Enter a positive number")
elif n==1:
  print(f)
elif n==2:
  print(f)
  print(s)  
else:
  print(f)
  print(s)  
  while i<=n:
    t=f+s
    print(t)
    f,s=s,t
    i+=1