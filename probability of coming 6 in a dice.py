import random
import statistics
l=[]
k=int(input("Enter number of times experiments to be performed "))
for i in range (0,k):
  n=0
  while True:
    s=random.randint(1,6)
    if s!=6:
      n+=1
    elif s==6:
      n+=1
      break
  l.append(n)
print("At which time 6 came in all experiments ",l)
x=statistics.mean(l)
print("At an average 6 comes at ",x,"th time")