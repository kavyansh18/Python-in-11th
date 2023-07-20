l=[]
while True:
  e=eval(input("Enter element for list "))
  l.append(e)
  ch=input("Press y/n to enter more elements ")
  if ch.upper()!='Y':
    break
print(l)