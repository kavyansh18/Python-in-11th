import random
AR=eval(input("Enter the list "))
Lower=random.randint(1,3)
Upper=random.randint(2,4)
for K in range(Lower, Upper +1):
 print (AR[K],end="#")