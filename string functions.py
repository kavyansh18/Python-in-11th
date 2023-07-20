n=input("Enter any string")
sp,v,c,d,s=0,0,0,0,0
for i in n:
  if i.isspace():
    sp+=1
  elif i.isalpha():
    if i in ("aeiou"):
      v+=1
    else:
      c+=1
  elif i.isdigit():
    d+=1
  else:
    s+=1
print("vowels =",v)
print("constants =",c)              
print("digits =",d)
print("spaces =",sp)
print("symbols =",s)