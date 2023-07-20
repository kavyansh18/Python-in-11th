s=0
k=0
n=int(input("Enter the number whose multiples are to be found"))
p=int(input("Enter number from where the multiples are to be found"))
r=int(input("Enter number till the multiples are to be found"))
for i in range(p,r):
  if i%n==0:
    s=s+1
    k=k+i
print(s,"is number of multiples between and",k, "is the sum of multiples betweeen")    

