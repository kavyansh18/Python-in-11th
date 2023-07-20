print("Lets Start")
print()
import random
kavyansh=0
system=0
while kavyansh!=100 or system!=100:
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
    print("kavyansh loose the game")
    break
  n1=random.randint(1,6)
  print("You got",n1)
  kavyansh+=n1
  if kavyansh==4:
   print("Congratulations! you got a ladder")
   system=14
  elif kavyansh==9:
   print("Congratulations! you got a ladder") 
   kavyansh=31
  elif kavyansh==2:
   print("Congratulations! you got a ladder") 
   kavyansh=38
  elif kavyansh==21:
   print("Congratulations! you got a ladder") 
   kavyansh=42
  elif kavyansh==28:
   print("Congratulations! you got a ladder") 
   kavyansh=84
  elif kavyansh==51:
   print("Congratulations! you got a ladder") 
   kavyansh=67
  elif kavyansh==72:
   print("Congratulations! you got a ladder") 
   kavyansh=91
  elif kavyansh==80:
   print("Congratulations! you got a ladder") 
   kavyansh=99
  if kavyansh==17:
   print("ohh no snake bitted you")
   kavyansh=7
  elif kavyansh==53:
   print("ohh no snake bitted you") 
   kavyansh=34
  elif kavyansh==62:
   print("ohh no snake bitted you") 
   kavyansh=19
  elif kavyansh==64:
   print("ohh no snake bitted you") 
   kavyansh=60
  elif kavyansh==87:
   print("ohh no snake bitted you") 
   kavyansh=36
  elif kavyansh==93:
   print("ohh no snake bitted you") 
   kavyansh=73
  elif kavyansh==95:
   print("ohh no snake bitted you") 
   kavyansh=75
  elif kavyansh==98:
   print("ohh no snake bitted you") 
   kavyansh=79
  print("kavyansh score =",kavyansh)
  print()
  if kavyansh>=100:
    print("kavyansh won the game")
    print("system loose the game")
    break
print()
print("Score of kavyansh is ",kavyansh)
print("Score of system is ",system)
print("GAME OVER")
