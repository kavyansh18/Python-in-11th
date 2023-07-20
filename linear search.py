l=[0,5,2,7,6,9,2,10,12,8]
n=int(input("Enter the keyword "))
for i in l:
  if i==n:
    print("Match found at ",l.index(i))
    break
else:
  print("Match not found")
