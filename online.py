import urllib.request
import urllib.error
from bs4 import BeautifulSoup
def SignUpURL(user, passwd):
    soup1=""
    try:
        r=urllib.request.urlopen(f"https://sharemarketgame.pythonanywhere.com/signup?user={user}&passwd={passwd}")
    except urllib.error.HTTPError as e:
            if e.code == 500:
                soup1="Fail"
    except urllib.error.URLError as r:
        soup1="Failed"
    else:
        soup1=BeautifulSoup(r,features="html.parser")
    print(soup1)
    return soup1

def loginURL(user, passwd):
    soup=""
    user=str(user)
    passwd=str(passwd)
    r=urllib.request.urlopen(f"https://sharemarketgame.pythonanywhere.com/login?user={user}&passwd={passwd}")
    test=BeautifulSoup(r, features="html.parser")
    if str(test) == "User not found!":
        soup = "no user"
    elif str(test) == "incorrect!":
        soup = "wrong password"
    else:
        soup="correct password"
    print(soup)
    return soup

def getInfoURL(username,typeOfInfo):
    r=urllib.request.urlopen(f"https://sharemarketgame.pythonanywhere.com/info?user={username}&type={typeOfInfo}")
    soup=BeautifulSoup(r, features="html.parser")
    return soup

def deleteUserURL(username):
    r=urllib.request.urlopen(f"https://sharemarketgame.pythonanywhere.com/deleteAccount?user={username}")
    soup=BeautifulSoup(r, features="html.parser")
    print(soup)

def updatePriceURL(stock):
    try:
        r=urllib.request.urlopen(f"https://sharemarketgame.pythonanywhere.com/getPrice?stock={stock}")
        soup=BeautifulSoup(r, features="html.parser")
    except urllib.error.HTTPError as e:
        return "No such stock"
    else:
        return str(soup)

def buyURL(username,stock,amount):
        r=urllib.request.urlopen(f"https://sharemarketgame.pythonanywhere.com/buy?user={username}&amount={amount}&stock={stock}")
        soup=BeautifulSoup(r, features="html.parser")
        return str(soup)

def sellURL(username,stock, amount):
        r=urllib.request.urlopen(f"https://sharemarketgame.pythonanywhere.com/sell?user={username}&amount={amount}&stock={stock}")
        soup=BeautifulSoup(r, features="html.parser")
        return str(soup)

def testping():
    try:
        r=urllib.request.urlopen("https://sharemarketgame.pythonanywhere.com/")
        soup=BeautifulSoup(r, features="html.parser")
    except urllib.error.HTTPError as e:
        if e.code==500:
            print("Server is down or being updated")
            return "Server is down or being updated"
    except urllib.error.URLError as r:
        return "Offline"
    else:
        if str(soup)=="Hello, rick!":
            print("Server is up!")
            return "Server is up!"
