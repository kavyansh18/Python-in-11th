import random
l2=[]
print("WELCOME TO KAVYANSH LOTTERY ")
print()
l1=list(input("Enter the lottery number(10 digits) "))
print()
k=input("Press enter for the first number ")
a=random.randint(0,9)
print("First number you got ",a)
l2.append(a)
if l1[0]==a:
  print()
  k=input("Press enter for the first number ")
  a=random.randint(0,9)
  print("Second number you got ",a)
  l2.append(a)
elif l1[0]!=a:
 print("OHH NO...BETTER LUCK NEXT TIME")
elif l1[1]==a:
 print()
 k=input("Press enter for the second number ")
 a=random.randint(0,9)
 print("Third number you got ",a)
 l2.append(a)
elif l1[1]!=a:
 print("OHH NO...BETTER LUCK NEXT TIME")
elif l1[2]==a:
 print()
 k=input("Press enter for the third number ")
 a=random.randint(0,9)
 print("Fourth number you got ",a)
 l2.append(a)
elif l1[2]!=a:
 print("OHH NO...BETTER LUCK NEXT TIME")
elif l1[3]==a:
 print()
 k=input("Press enter for the fourth number ")
 a=random.randint(0,9)
 print("Fifth number you got ",a)
 l2.append(a)
elif l1[3]!=a:
  print("OHH NO...BETTER LUCK NEXT TIME")
elif l1[4]==a:
 print()
 k=input("Press enter for the fifth number ")
 a=random.randint(0,9)
 print("Sixth number you got ",a)
 l2.append(a)
elif l1[4]!=a:
 print("OHH NO...BETTER LUCK NEXT TIME")
elif l1[5]==a:
 print()
 k=input("Press enter for the sixth number ")
 a=random.randint(0,9)
 print("Seventh number you got ",a)
 l2.append(a)
elif l1[5]!=a:
 print("OHH NO...BETTER LUCK NEXT TIME")
elif l1[6]==a:
 print()
 k=input("Press enter for the seventh number ")
 a=random.randint(0,9)
 print("Eighth number you got ",a)
 l2.append(a)
elif l1[6]!=a:
 print("OHH NO...BETTER LUCK NEXT TIME")
elif l1[7]==a:
 print()
 k=input("Press enter for the eighth number ")
 a=random.randint(0,9)
 print("Nineth number you got ",a)
 l2.append(a)
elif l1[7]!=a:
 print("OHH NO...BETTER LUCK NEXT TIME")
elif l1[8]==a:
 print() 
 k=input("Press enter for the first number ")
 a=random.randint(0,9)
 print("Tenth number you got ",a)
 l2.append(a)
elif l1[8]!=a:
 print("OHH NO...BETTER LUCK NEXT TIME")
elif l1[9]==a:
 print("CONGRATULATIONS!!!...YOU WON THE LOTTERY ")
elif l1[9]!=a:
 print("OHH NO...BETTER LUCK NEXT TIME")
print()
print("THANKS FOR COMING")