n=list(input("Enter the numbers  "))
k=[]
s=n[::2]
s1=n[1::2]
while s!=[] or s1!=[]:
  if s1!=[]:
    k.append(s1.pop(0))
  elif s!=[]:
    k.append(s.pop(0))
print(n)
print(k)