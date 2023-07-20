n=int(input("Enter number of terms "))
x=int(input("Enter the value of x"))
s=0
print("1 +",end="")
print( x,end="")
s+=x
for i in range(2,n+1):
  print("+",x,"^",i,end="")
  s=s+(1+x**i)
print()  
print("Sum of the series = ",s)  
