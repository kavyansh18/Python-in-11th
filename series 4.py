n=int(input("Enter number of terms "))
x=int(input("Enter the start value"))
s=0
print(x,end="")
s+=x
for i in range(2,n+1):
  f=1
  for j in range(1,i+1):
    f+=1
  if i%2==0:
    print("+",x,"^",i,"/",f,end="")
  else:
    print("-",x,"^",i,"/",f,end="")    
  s=s+(x**i*(-1)**i/f)
print()  
print("Sum of the series = ",s)  
