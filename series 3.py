n=int(input("Enter number of terms "))
x=int(input("Enter the value of x"))
s=0
print("1 +",end="")
print( x,end="")
s+=x
for i in range(2,n+1):
  if i%2==0:
    print("+",x,"^",i,end="")
  else:
    print("-",x,"^",i,end="")    
  s=s+(1+x**i*(-1))
print()  
print("Sum of the series = ",s)  
