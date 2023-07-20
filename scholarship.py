n=input("Enter your gender M/F")
m=int(input("Enter your marks"))
if(n=="M"):
  if(100>=m>=75):
    print("Congratulations!!!, You are eligible for the scholarship")
  else:
    print("You are not eligible")
else:
  if(100>=m>=65):
    print("Congratulations!!!, You are eligible for the scholarship")
  else:
    print("You are not eligible")  
print("Best of luck!")    