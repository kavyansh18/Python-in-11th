a=int(input("Enter first number "))
k=input("Enter the operation ")
b=int(input("Enter second number "))
if k=='+':
  c=a+b
  print(c)
elif k=='-':
  c=a-b
  print(c)
elif k=='x':
  c=a*b
  print(c)
elif k=='/':
  c=a/b
  print(c)
elif k=='^':
  c=a**b
  print(c)