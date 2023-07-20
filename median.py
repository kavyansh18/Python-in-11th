l=eval(input('list of integers'))
l1=sorted(l)
t=len(l)
if t%2==0: 
  k=l1[t//2]
  s=l1[t//2]-1
  print ('median is',(k+s)/2)
else:
 a=l1[t//2]
 print ('median is',a)