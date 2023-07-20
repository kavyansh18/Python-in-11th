l=eval(input("Enter the list: "))
print("Original List is:",l)
s=len(l)
if s%2!=0:
    s=s-1
for i in range(0,s,2):
    l[i],l[i+1]=l[i+1],l[i]
print("List after swapping :",l)
