import random
print("WELCOME TO KAVYANSH LOTTERY ")
print()
l1=list(input("Enter the lottery number(10 digits) "))
s=len(l1)
if s!=10:
  print("INVALID")
else:
  l2=[]
  print()
  q=input("Press enter to try your luck ")
  print()
  a=random.randint(0,9)
  l2.append(a)
  a=random.randint(0,9)
  l2.append(a)
  a=random.randint(0,9)
  l2.append(a)
  a=random.randint(0,9)
  l2.append(a)
  a=random.randint(0,9)
  l2.append(a)
  a=random.randint(0,9)
  l2.append(a)
  a=random.randint(0,9)
  l2.append(a)
  a=random.randint(0,9)
  l2.append(a)
  a=random.randint(0,9)
  l2.append(a)
  a=random.randint(0,9)
  l2.append(a)
  if l1==l2:
   print("CONGRALUTAIONS!!!...YOU WON THE LOTTERY ")  
  else:
   print("OHH NO, BETTER LUCK NEXT TIME")   
print() 
print("THANKS FOR COMING")    
