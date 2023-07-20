i=1
d={}
while True:
  r=int(input("Enter the roll number "))
  name=input("Enter the name ")
  m=int(input("Enter the marks "))
  d[i]=[r,name,m]
  i+=1
  x=input("Enter 'y' to enter more records and 'n' to stop")
  if x=='n':
    break
print()
for i in d:
  print(i, d[i])
print()
for i in d:
  if d[i][2]>75:
    print("Student(s) scored above 75 ")
    print(d[i][1])