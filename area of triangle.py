a=int(input("First side of triangle"))
b=int(input("Second side of triangle"))
c=int(input("Third side of triangle"))
s=(a+b+c)/2
h=((s)*(s-a)*(s-b)*(s-c))**1/2
print("The area of triangle is",h)