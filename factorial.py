s=1
n=int(input("Enter the number"))
if(n<0):
  print("Please enter a positive number")
else:
 for i in range(1,n+1):
    s=s*i
 print(s)  
