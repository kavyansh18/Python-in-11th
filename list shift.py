l=[10,20,30,40,50,60,70,80,90]
s=int(input("Enter the number of element(s) to be shifted toward left "))
print(l)
for i in range(1,s+1):
  t=l.pop(0)
  l.append(t)
print(l)