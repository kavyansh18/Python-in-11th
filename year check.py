n=int(input("Enter the year"))
if(n%100==0):
  if(n%400==0):
    print("the year is century year")
  else:
    print("the year is not a century year")  
else:
  if(n%4==0):
    print("the year is leap year")
  else:
    print("the year is century year but not a leap year")  