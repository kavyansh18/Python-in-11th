n=int(input('Enter the number'))
s=2
while n!=1:
  if n%s==0:
    n/=s
    print(s)
  else:
    s+=1
    
