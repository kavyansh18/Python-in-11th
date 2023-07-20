l=eval(input("Enter the list "))
odd=[]
even=[]
for i in l:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print("Number of even elements",len(even),even)
print("Number of odd elements",len(odd),odd)