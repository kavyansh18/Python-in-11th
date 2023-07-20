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
  print("system score =",system)
  print()
  if system>=100:
    print("system won the game")
    break
  d=input("Press enter to roll your chance ")
  print()
  n1=random.randint(1,6)
  print(a," got",n1)
  a1+=n1
  print(a," score =",a1)
  print()
  if a1>=100:
    print(a," won the game")
    break
  e=input("Press enter to roll your chance ")
  print()
  n1=random.randint(1,6)
  print(b," got",n1)
  b1+=n1
  print(b," score =",b1)
  print()
  if b1>=100:
    print(b," won the game")
    break
  y=input("Press enter to roll your chance ")
  print()
  if y=='3':
    n1=random.randint(1,6)
    print(c," got",n1)
    c1+=n1
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
