n=int(input("enter the speed"))
if(n>140):
  print("Your driving licence is canceled")
else:
  if(n>120):
    print("Pay fine of Rs.5000/-")
  else:
    if(n>100):
      print("Pay fine of Rs.2000/-")
    else:
      if(n>80):
        print("Pay fine of Rs.1000/-")
      else:
        if(n<0):
          print("speed can not be in negative")
        else:
          print("NO FINE")