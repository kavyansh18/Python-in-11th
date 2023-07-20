import random
l1=list(input("Enter the lottery number(5 digits) "))
l2=[]
if len(l1)!=5:
 print("INVALID")
else:
  for i in range(5):
   n=input("Press enter to try your luck ")
   k=random.randint(0,9)
   print("You got ",k)
   print()
   l2.append(k)
  l1.sort()
  l2.sort()
  if l1==l2:
   print('CONGRATULATIONS!!!...TOU WON THE LOTTERY')
  elif l1!=l2:
   print("ohh no...BETTER LUCK NEXT TIME")