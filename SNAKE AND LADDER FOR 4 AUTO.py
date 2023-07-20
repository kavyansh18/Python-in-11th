print("Lets Start")
print()
import random
a=input("Enter name of 1st player  ")
b=input("Enter name of 2nd player  ")
c=input("Enter name of 3rd player  ")
print()
a1=0
system=0
b1=0
c1=0
while a1!=100 or system!=100 or b1!=100 or c1!=0:
  n=random.randint(1,6)
  print("system got",n)
  system+=n
  if system==4:
   print("System got a ladder")
   system=14
  elif system==9:
   print("System got a ladder") 
   system=31
  elif system==2:
   print("System  got a ladder") 
   system=38
  elif system==21:
   print("System got a ladder") 
   system=42
  elif system==28:
   print("System got a ladder") 
   system=84
  elif system==51:
   print("System got a ladder") 
   system=67
  elif system==72:
   print("System got a ladder") 
   system=91
  elif system==80:
   print("System got a ladder") 
   system=99
  if system==17:
   print("snake bitted system")
   system=7
  elif system==53:
   print("snake bitted system") 
   system=34
  elif system==62:
   print("snake bitted system") 
   system=19
  elif system==64:
   print("snake bitted system") 
   system=60
  elif system==87:
   print("snake bitted system") 
   system=36
  elif system==93:
   print("snake bitted system") 
   system=73
  elif system==95:
   print("snake bitted system") 
   system=75
  elif system==98:
   print("snake bitted system") 
   system=79
  print("system score =",system)
  print()
  if system>=100:
    print("system won the game")
    break
  n1=random.randint(1,6)
  print(a," got",n1)
  a1+=n1
  if a1==4:
   print("Congratulations!",a," got a ladder")
   a1=14
  elif a1==9:
   print("Congratulations!",a," got a ladder") 
   a1=31
  elif a1==2:
   print("Congratulations!",a," got a ladder") 
   a1=38
  elif a1==21:
   print("Congratulations!",a," got a ladder") 
   a1=42
  elif a1==28:
   print("Congratulations!",a," got a ladder") 
   a1=84
  elif a1==51:
   print("Congratulations!",a," got a ladder") 
   a1=67
  elif a1==72:
   print("Congratulations!",a," got a ladder") 
   a1=91
  elif a1==80:
   print("Congratulations!",a," got a ladder") 
   a1=99
  elif a1==17:
   print("ohh no snake bitted ",a)
   a1=7
  elif a1==53:
   print("ohh no snake bitted ",a) 
   a1=34
  elif a1==62:
   print("ohh no snake bitted ",a)
   a1=19
  elif a1==64:
   print("ohh no snake bitted ",a) 
   a1=60
  elif a1==87:
   print("ohh no snake bitted ",a) 
   a1=36
  elif a1==93:
   print("ohh no snake bitted ",a) 
   a1=73
  elif a1==95:
   print("ohh no snake bitted ",a) 
   a1=75
  elif a1==98:
   print("ohh no snake bitted ",a) 
   a1=79
  print(a," score =",a1)
  print()
  if a1>=100:
    print(a," won the game")
    break
  n1=random.randint(1,6)
  print(b," got",n1)
  b1+=n1
  if b1==4:
   print("Congratulations!",b," got a ladder")
   b1=14
  elif b1==9:
   print("Congratulations!",b," got a ladder") 
   b1=31
  elif b1==2:
   print("Congratulations!",b," got a ladder") 
   b1=38
  elif b1==21:
   print("Congratulations!",b," got a ladder") 
   b1=42
  elif b1==28:
   print("Congratulations!",b," got a ladder") 
   b1=84
  elif b1==51:
   print("Congratulations!",b," got a ladder") 
   b1=67
  elif b1==72:
   print("Congratulations!",b," got a ladder") 
   b1=91
  elif b1==80:
   print("Congratulations!",b," got a ladder") 
   b1=99
  elif b1==17:
   print("ohh no snake bitted ",b)
   b1=7
  elif b1==53:
   print("ohh no snake bitted ",b) 
   b1=34
  elif b1==62:
   print("ohh no snake bitted ",b) 
   b1=19
  elif b1==64:
   print("ohh no snake bitted ",b) 
   b1=60
  elif b1==87:
   print("ohh no snake bitted ",b) 
   b1=36
  elif b1==93:
   print("ohh no snake bitted ",b) 
   b1=73
  elif b1==95:
   print("ohh no snake bitted ",b) 
   b1=75
  elif b1==98:
   print("ohh no snake bitted ",b) 
   b1=79
  print(b," score =",b1)
  print()
  if b1>=100:
    print(b," won the game")
    break
  n1=random.randint(1,6)
  print(c," got",n1)
  c1+=n1
  if c1==4:
   print("Congratulations!",c," got a ladder")
   c1=14
  elif c1==9:
   print("Congratulations!",c," got a ladder") 
   c1=31
  elif c1==2:
   print("Congratulations!",c," got a ladder") 
   c1=38
  elif c1==21:
   print("Congratulations!",c," got a ladder") 
   c1=42
  elif c1==28:
   print("Congratulations!",c," got a ladder") 
   c1=84
  elif c1==51:
   print("Congratulations!",c," got a ladder") 
   c1=67
  elif c1==72:
   print("Congratulations!",c," got a ladder") 
   c1=91
  elif c1==80:
   print("Congratulations!",c," got a ladder") 
   c1=99
  elif c1==17:
   print("ohh no snake bitted ",c)
   c1=7
  elif c1==53:
   print("ohh no snake bitted ",c) 
   c1=34
  elif c1==62:
   print("ohh no snake bitted ",c) 
   c1=19
  elif c1==64:
   print("ohh no snake bitted ",c) 
   c1=60
  elif c1==87:
   print("ohh no snake bitted ",c)
   c1=36
  elif c1==93:
   print("ohh no snake bitted ",c) 
   c1=73
  elif c1==95:
   print("ohh no snake bitted ",c) 
   c1=75
  elif c1==98:
   print("ohh no snake bitted ",c) 
   c1=79
  print(c," score =",c1)
  print()
  if c1>=100:
    print(c," won the game")
    break
print()
print("Score of ",a," is ",a1)
print("Score of system is ",system)
print("Score of ",b," is ",b1)
print("Score of ",c," is ",c1)
print("GAME OVER")
