print("Lets Start")
print()
import random
kavyansh=0
system=0
anu=0
shirin=0
while kavyansh!=100 or system!=100 or anu!=100 or shirin!=0:
  n=random.randint(1,6)
  print("system got",n)
  system+=n
  print("system score =",system)
  print()
  if system>=100:
    print("system won the game")
    break
  d=input("Press enter to roll your chance ")
  print()
  n1=random.randint(1,6)
  print("Kavyansh got",n1)
  kavyansh+=n1
  print("kavyansh score =",kavyansh)
  print()
  if kavyansh>=100:
    print("kavyansh won the game")
    break
  e=input("Press enter to roll your chance ")
  print()
  n1=random.randint(1,6)
  print("Anu got",n1)
  anu+=n1
  print("anu score =",anu)
  print()
  if anu>=100:
    print("anu won the game")
    break
  c=input("Press enter to roll your chance ")
  print()
  n1=random.randint(1,6)
  print("Shirin got",n1)
  shirin+=n1
  print("Shirin score =",shirin)
  print()
  if shirin>=100:
    print("shirin won the game")
    break
print()
print("Score of kavyansh is ",kavyansh)
print("Score of system is ",system)
print("Score of anu is ",anu)
print("Score of shirin is ",shirin)
print("GAME OVER")
