
s=1
n=int(input("Enter the number whose multiples are to be found"))
p=int(input("Enter number of multiples to be found"))
r=int(input("Enter number from which multiples are to be found"))
if(r%n==0):
  for i in range(r,(((p*n)+n)+r),n):
   print(s*i)
else:
  r=r+(n-(r%n))
  for i in range(r,(((p*n)+n)+r),n):
   print(s*i)
