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
  print("system score =",system)
  print()
  if system>=100:
    print("system won the game")
    print(s," loose the game")
    break
  d=input("Press enter to roll your chance ")
  print()
  n1=random.randint(1,6)
  print(s," got",n1)
  k+=n1
  print(s," score =",k)
  print()
  if k>=100:
    print(s," won the game")
    print("system loose the game")
    break
print()
print("Score of ",s," is ",k)
print("Score of system is ",system)
print("GAME OVER")
