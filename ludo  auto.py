print("Lets Start")
print()
import random
kavyansh=0
system=0
while kavyansh!=100 or system!=100:
  n=random.randint(1,6)
  print("system got",n)
  system+=n
  print("system score =",system)
  print()
  if system>=100:
    print("system won the game")
    print("kavyansh loose the game")
    break
  n1=random.randint(1,6)
  print("You got",n1)
  kavyansh+=n1
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
