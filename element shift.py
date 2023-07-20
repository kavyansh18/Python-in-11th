l=[10,20,30,40,50,60,70,80,90]
s=int(input("Enter the element to be shifted "))
if s not in l:
  print(s, "is not an element of list")
else:
  k=int(input("Enter at which place the element is to be shifted "))
if s in l:
  l.remove(s)
  l.insert(k-1,s)
  print(l)
