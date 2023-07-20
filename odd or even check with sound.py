
from playsound import playsound
n=int(input("enter an integer number:"))
if(n%2==0):
  print(n,"is an even number")
  playsound('even.mp3')
else:
  print(n,"is an odd number")
  playsound('odd.mp3')
  
