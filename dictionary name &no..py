n=int(input("Enter no of key pair values "))
x={}
print()
print("Phone number is taken as key ")
print("Name is used as key values")
print()
for i in range(n):
  k=int(input("Enter the phone number "))
  s=input("Enter the name ")
  x[k]=s
print(x)