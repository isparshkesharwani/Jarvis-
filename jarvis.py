
#---------------------------------------------------------------------------jarvir--------------------------------------------------------------------------
#Program infomation
#Jarvis version -- 0.1.3
#This program is complete
#This progrome crater name = Isparsh Kesharwani




import time
coin=5000
print ("hello sir")
print ('''
      1 == Hii
      '''
      )
try:
     option=int(input("please enter your choise "))
except:
        print("please enter valid option")

if option==1:
    print ("how are you")

    print ('''
           3 == I am fine what about you
           '''
           )
try:
     option=int(input("please enter your choise "))
except:
        print("please enter valid option")

if option==3:

    print ("I am also fine")

    print (f"what is your name")

    name=input("enter name ")

    print (f"This name is vary cool")

    print ('''
          T == thank you
          t == thanks
          '''
          )
try:
     option=int(input("please enter your choise "))
except:
        print("wellcome")

        print ('''
              W == whatr is your name

              '''
              )
try:
     option=int(input("please enter your choise "))
except:
        print("ok")

        print ("my name is jarvis")
        print ("can i help you")
        print ('''
              4 == no
              5 == play game
              6 == play jock
              '''
              )
try:
     option=int(input("please enter your choise "))
except:
        print("ok")

if option==4:
    print ("exit=x")
    no=input("enter a number")
    time(500)

if option==5:
    print ('''
          Hello sir.
          Sir please choose the game.
          '''
          )


    print ('''
          7 == 2 latter passwords cutter
          '''
          )
try:
     option=int(input("please enter your choise "))
except:
        print("ok")

if option==8:
    print ("your 1st game is and your 2nd game is start")
    print ('''
          Hello sir
          Sir please choose your cest
          How to play
          1. buy cest.
          2. Cest option
             gold cest %99
             silver cest %50
             rock cest %25
          3. How to win this game
          buy the cest and oprnto win coin .
          '''
          )

print ('''
      00 == chack coin
      11 == play game
      '''
      )
try:
     option=int(input("please enter your choise "))
except:
        print("ok")
if option==00:
    print (f"your balance is {coin}")
    print ('''
          11 == play game
          '''
          )
try:
     option=int(input("please enter your choise "))
except:
        print("ok")



if option==11:
    print ('''
          22 == gold cest rs 500
          33 == silver cest rs 300
          44 == roct cest rs 100
          '''
          )
try:
     option=int(input("please enter your choise "))
except:
        print("ok")
if option==22:

    print (f"-500")

    coin=coin-500

    print (f"+800")

    coin=coin+800

    print (f"you have are a winer")
if option==33:

    print ("-300")

    coin=coin-300

    print ("+200")

    print ("game over")

if option==44:

    print ("-100")

    coin=coin-100

    print ("+300")

    coin=coin+300

    print ("you have winer")



if option==7:

 from random import *
user_pass = input("Enter your password")
password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guess = ""
while(guess!=user_pass):
    guess = ""
    for letter in range (len(user_pass)):
        guess_letter = password[randint(0,25)]
        guess = str(guess_letter)+str(guess)
        print(guess)
print('your password is ',guess)
print ("This game is complete")
print ("Thanks foer cooming")
