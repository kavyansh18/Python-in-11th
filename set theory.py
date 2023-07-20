menu='''
 1.UNION
 2.INTERSECTION
 3.A-B
 4.B-A
 5.EXIT
'''
while True:
  print(menu)
  c=int(input("Enter the choice "))
  if c==1:
    l1=eval(input("Enter the list 1 "))
    l2=eval(input("Enter the list 2 "))
    l3=[]
    for i in l1:
      if i not in l3:
        l3.append(i)
    for i in l2:
      if i not in l3:
        l3.append(i)
    print("Union = ",l3)
  elif c==2:
    l1=eval(input("Enter the list 1 "))
    l2=eval(input("Enter the list 2 "))
    l3=[]
    for i in l1:
      if i in l2 and i not in l3:
        l3.append(i)
    print("Intersection = ",l3)      
  elif c==3:
   l1=eval(input("Enter the list 1 "))
   l2=eval(input("Enter the list 2 "))
   l3=[]
   for i in l1:  
    if i not in l2 and i not in l3:
      l3.append(i)
    print("A-B = ",l3)  
  elif c==4:
   l1=eval(input("Enter the list 1 "))
   l2=eval(input("Enter the list 2 "))
   l3=[]
   for i in l1:  
    if i not in l1 and i not in l3:
      l3.append(i)
    print("B-A = ",l3) 
  elif c==5:
    break
  else:
    print("INVALID") 