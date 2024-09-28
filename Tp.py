# Stock Market Game

# By: Kaan Alp Gökozan
# Discord: kaanalp28#8306

import random
import time
import os

splash = ["Buy Low and Sell High for HUGE GAINS!!!","'Stock Market Game is the best financial trainer out there'- Warren Buffet","Possibly the best game on Replit?","Tell me in the comments how much you made, I'd love to hear it!","If only these were possible in real life!","Did you hear about that hamster that outperformed the S&P 500!!!","Thank You for playing my game! :)","Best of luck out there!","Shout-out to OwenBlack!","Thanks to OwenBlack for making a LEGENDARY game! I just made the Python version, the idea is completely OwenBlack's!!!","I'm curious where are you guys from? Tell me in the comments!","What do you guys like about this game and are there any bugs that I need to fix, Tell me in the comments!","'The best trainer for all diamond holding apes'-r/wallstreetbets","Just a reminder, you're the best!","Like the new update?","Notch!","As seen on TV!","SPLASH!"]

print("Thanks to OwenBlack for making a LEGENDARY game! I just made the Python version, the idea is completely OwenBlack's!!!")

randSplash = random.randrange(len(splash))
randText = splash[randSplash]

print("\n\nIn this game your goal is to buy low and sell high for HUGE gains in the stock market\n\n")

while True:
  try:
    days = int(input("How many days would you like to play the stock market for?: "))
    break
  except ValueError:
    print("-\nPlease input integer only...")  
    print("----------")

time.sleep(0.25)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

clearConsole()

i=0
average=0
avg=0
times=0
share=0
bal=1000

while i < int(days):
  left=int(days)-i
  print(" ____  _____ |||||| ______     __   __    ____\n/        |   |    | |     |   | |  / /   /     \n|        |   |    | |     |   | | / /    |     \n ----    |   |    | |     |   | |/ /      ---- \n     |   |   |    | |     |   | |_ _          |\n    /    |   |    | |     |   | | _ _        / \n----     |   |||||| |     |   | |  _ _   ----  ")
  print("["+randText+"]")
  print("\n============================================================================================\n")
  print("Days Left: "+str(left), end='   -   ')
  print("Balance: $"+str(bal), end='   -   ')
  print("Shares: "+str(share), end='   -   ')
  print("Average Buy Cost: $"+str(avg))
  print(" \n")
  stock=random.randint(1,1100)
  print("Today's stock price: $"+str(stock))
  i=i+1
  maxbuy=(bal/stock)
  maxbuy=int(maxbuy)
  invest=str(input("\nWhat would you like to do?    Buy(1)?    Sell(2)?    Or wait to the next day(3)?\n\nYour Choice?: "))
  print("\n----------")
  if(invest=="1"):
    print("The max amount of shares you can buy is: "+str(maxbuy)+"\n----------")
    print("If you want to buy max shares type '12345'.\n-")
    amount=int(input("How many shares would you like to buy?: "))
    print("----------")
    if(str(amount)=="12345"):
      amount=maxbuy
    elif(amount>maxbuy):
      print("----------\nHEY THERE! STOP! Do you forget? You don't have enough money... I'm buying the max amount you can afford instead.")
      amount=maxbuy
      time.sleep(1.75)
    elif(amount<0):
      print("So you find the bug on the original version, and tried it here? NOPE too late... Maybe if you played this in the first day it got released...")
      print("As a result, I'm skipping this day!")
      amount=0
      time.sleep(5)
    bal=(bal-amount*stock)
    share=(share+amount)
    if(maxbuy>0):
      if(amount>0):
        if(amount==12345):
          times=times+1
          average=average+stock
        else:
          times=times+1
          average=average+stock

  elif(invest=="2"):
    print("The max amount of shares you can sell is "+str(share)+".\n----------")
    print("If you would like to sell all of your shares type '12345', else...")
    sell=int(input("How many shares would you like to sell?: "))
    if(str(sell)=="12345"):
      sell=share
      bal=bal+sell*stock
      share=share-sell
    elif(sell>share):
      print("----------\n\nBRUH how are you supposed to sell the money you don't even OWN?\n\n----------")
      time.sleep(1.5)
    elif(sell<0):
      print("So you find the bug on the original version, and tried it here? NOPE too late... Maybe if you played this in the first day it got released...")
      print("As a result, I'm skipping this day!")
      time.sleep(5)
    else:
     bal=bal+sell*stock
     share=share-sell
  else:
    print("You skipped the day... Don't you feel USELESS sometimes?!")
    time.sleep(0.675)
  if(times>0):
    avg=average/times
    avg=int(avg)
  def clearConsole():
      command = 'clear'
      if os.name in ('nt', 'dos'): 
          command = 'cls'
      os.system(command)

  clearConsole()
    
if(share>0):
  lprice=random.randint(50,1050)
  print("Last day's stock price: "+str(lprice)+"\n----------")
  convert=int(input("Would you like me to convert your shares to dollars using the last share price? Yes(1) No(2): "))
  if(convert==1):
    bal=(bal+share*int(lprice))
    share=0

print("----------\n\nYou have 0 days left to make money. Lets see how you did!\n\n----------")

print("\nAfter "+str(days)+" days you have made $"+str(bal)+" dollars.\n\n-")
print("\nYou own "+str(share)+" shares.\n\n----------")
if(bal<1000):
  print("\n\nYOU LOST THE MONEY!!! Oh well... Back to McDonald's I guess...")
elif(bal==1000):
  print("\n\nAre you sure that you played the game at all?!?!?!")
elif(bal<1000000):
  print("\n\nPretty good but I think you can do better, maybe if you play for longer?!")
elif(bal<1000000000):
  print("\n\nWOW WOW WOW, very good indeed. Very stonks!")
elif(bal<1000000000000):
  print("\n\nCan you teach me your ways? Because that was amazing!")
else:
  print("\n\nVERY VERY Impressive!!! Now just do that in the real world and you will be set ;)")