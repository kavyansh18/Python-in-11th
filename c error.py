a=int(input("Enter first number "))
k=input("Enter the operation ")
b=int(input("Enter second number "))
while True:
 if k=='+':
  c=a+b
  print(c)
  z=int(input("Enter the number "))
  print(c+z)
 elif k=='-':
  c=a-b
  print(c)
  z=int(input("Enter the number "))
  print(c-z)
 elif k=='x':
  c=a*b
  print(c)
  z=int(input("Enter the number "))
  print(c*z)
 elif k=='/':
  c=a/b
  print(c)
  z=int(input("Enter the number "))
  print(c/z)
 elif k=='^':
  c=a**b
  print(c)
  z=int(input("Enter the number "))
  print(c**z)