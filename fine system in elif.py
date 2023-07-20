n=int(input("enter the speed"))
if(n>140):
  print("Your driving licence is canceled")
elif(n>120):
  print("Pay fine of Rs.5000/-")
elif(n>100):
  print("Pay fine of Rs.2000/-")
elif(n>80):
  print("Pay fine of Rs.1000/-")
elif(n<0):
  print("speed can not be in negative")
else:
 print("NO FINE")