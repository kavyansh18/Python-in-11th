n=int(input("Enter your marks"))
if(n>100):
  print("marks can not be grater than 100")
else:
  if(n>90):
    print("A+ Grade")
  else:
    if(n>75):
      print("A Grade")
    else:
      if(n>60):
        print("B Grade")
      else:
        if(n>45):
          print("C Grade")
        else:
         if(n>32):
          print("D Grade")
         else:
           if(n>=0):
             print("E Grade")
           else:
              print("marks can not be less than zero") 
