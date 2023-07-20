a=list(input("Enter the equation without gaps and with only one operation "))
if a[1]=='x':
  b=int(a[0])*int(a[2])
  print(b)
elif a[1]=='+':
  b=int(a[0])+int(a[2])
  print(b)
elif a[1]=='-':
  b=int(a[0])-int(a[2])
  print(b)
elif a[1]=='/':
  b=int(a[0])/int(a[2])
  print(b)
elif a[1]=='^':
  b=int(a[0])**int(a[2])
  print(b)