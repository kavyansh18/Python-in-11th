from playsound import playsound
menu='''
 1.AADI EK CHIRIYA
 2.SCAM 1992
 3.SQUID GAME
 4.SUCH A WHORE
 5.GALAXY
'''
print(menu)
k=int(input("Enter the choice"))
if k==1:
      playsound('aadi.mp3')
elif k==2:
      playsound('scam.mp3')
elif k==3:
      playsound('squid.mp3')
elif k==4:
      playsound('whore.mp3')
elif k==5:
      playsound('galaxy.mp3')
