l=[0,5,2,7,6,9,2,10,12,8,5,1,2,4,8,2,7,2,2,5]
s=[]
for i in l:
  if i not in s:
    s.append(i)
print(s)
for i in s:
  print(i, l.count(i))
print("Average", sum(l)/len(l)) 

