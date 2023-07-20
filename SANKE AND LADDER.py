
print("Lets Start")
print()
import random
s=input("Enter name of player  ")
k=0
system=0
while k!=100 or system!=100:
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
  elif system==17:
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
    print(s," loose the game")
    break
  d=input("Press enter to roll your chance ")
  print()
  n1=random.randint(1,6)
  print("You got",n1)
  k+=n1
  if k==4:
   print("Congratulations! you got a ladder")
   system=14
  elif k==9:
   print("Congratulations! you got a ladder")
   k=31
  elif k==2:
   print("Congratulations! you got a ladder")
   k=38
  elif k==21:
   print("Congratulations! you got a ladder")
   k=42
  elif k==28:
   print("Congratulations! you got a ladder")
   k=84
  elif k==51:
   print("Congratulations! you got a ladder")
   k=67
  elif k==72:
   print("Congratulations! you got a ladder")
   k=91
  elif k==80:
   print("Congratulations! you got a ladder")
   k=99
  if k==17:
   print("ohh no snake bitted you")
   k=7
  elif k==53:
   print("ohh no snake bitted you")
   k=34
  elif k==62:
   print("ohh no snake bitted you")
   k=19
  elif k==64:
   print("ohh no snake bitted you")
   k=60
  elif k==87:
   print("ohh no snake bitted you")
   k=36
  elif k==93:
   print("ohh no snake bitted you")
   k=73
  elif k==95:
   print("ohh no snake bitted you")
   k=75
  elif k==98:
   print("ohh no snake bitted you")
   k=79
  print(s," score =",k)
  print()
  if k>=100:
    print(s," won the game")
    print("system loose the game")
    break
print()
print("Score of",s,"is",k)
print("Score of system is ",system)
print("GAME OVER")
