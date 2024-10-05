import time
import connect
import online
from tkinter import *
import os
import threading

def cScreen(frame):
    for widget in frame.winfo_children():
        widget.destroy()

stockNames=["Apple", "Google", "Amazon", "Nestle", "Toyota"]

stop=False

def priceUpdate(plabel, stock):
    while True:
        f=online.updatePriceURL(stock)
        plabel.config(text=f)
        time.sleep(5)
        if stop:
            break

def exiting(win):
    cScreen(win)
    win.title("Exiting...")
    frame=Frame(win)
    exitLabel=Label(frame, text="Quiting Threads...", font=("Helvetica", 10), background="black", foreground="white")
    exitLabel.pack()
    frame.place(relx=0.5, rely=0.5, anchor="c")
    win.after(2000, func=quit)
    
def exitFunc(wind):
    global stop
    stop=True
    exiting(wind)

def  exitThread(name, win):
    global stop
    stop=True
    gameStart(name, win)

def tryAgainBuyStock(stock, name, win):
    win.destroy()
    buyStock(stock, name)

def buyStockBack(stock, name, amountText, win):
    amount=amountText.get()
    cScreen(win)
    try:
        amount=int(amount)
    except:
        f=Frame(win, background="black")
        text=Label(f, text="Enter a valid number, only whole numbers", font=("Helvetica", 10), background="black", foreground="white")
        text.pack()
        tryAgain=Button(f, text="Try again", command=lambda: tryAgainBuyStock(stock, name, win), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
        tryAgain.pack()
        f.place(relx=0.5, rely=0.5, anchor="c")
    else:
        print(f"Stock: {stock}, Name: {name}, amount: {amount}")
        win.destroy()

def buyStock(stock, name):
    window=Tk(className="Buy Stock")
    window.geometry("400x300")
    window.config(background="black")
    f=Frame(window, background="black")
    label=Label(f, text=f"Buy stocks of {stockNames[stock-1]}", font=("Helvetica", 10), background="black", foreground="white")
    label.pack(pady=2.5)
    amtLabel=Label(f, text="Enter Amount: ", font=("Helvetica", 10), background="black", foreground="white")
    amtLabel.pack(pady=2.5)
    amount=Entry(f, font=("Helvetica", 10), background="#8A8A8A", foreground="white", width=5)
    amount.pack(pady=2.5)
    sub=Button(f, text="Buy", command=lambda: buyStockBack(stock, name, amount, window), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    sub.pack(pady=2.5)
    cancel=Button(f, text="Cancel", command=window.destroy, font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    cancel.pack(pady=2.5)
    f.place(relx=0.5, rely=0.5, anchor="c")

def startStock(stock, win,name):
    global price
    cScreen(win)
    nameText=Label(win, text=name, font=("Helvetica", 10), background="black", foreground="white")
    nameText.pack(side=TOP, anchor="e")
    win.title(stockNames[stock-1])
    win.config(background="black")
    frame=Frame(win)
    frame.config(background="black")
    priceLabel=Label(frame, text="Fetching Price...", font=("Helvetica", 10), background="black", foreground="white")
    priceLabel.pack(pady=2.5)
    price=threading.Thread(target=lambda: priceUpdate(priceLabel, stock))
    price.start()
    buyBut=Button(frame, text="Buy", command=lambda: buyStock(stock, name), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    buyBut.pack(pady=2.5)
    backBut=Button(frame, text="Main Menu", command=lambda: exitThread(name, win), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    backBut.pack(pady=2.5)
    x=Button(frame,text="Quit", command=lambda: exitFunc(win), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    x.pack(pady=2.5)
    frame.place(relx=0.5, rely=0.5, anchor="c")

def checkProfile(typeOfInfo, win, name):
    cScreen(win)
    nameText=Label(win, text=name, font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    nameText.pack(side=TOP, anchor="e")
    frame=Frame(win, background="black")
    win.configure(background="black")
    x=online.getInfoURL(name, typeOfInfo)
    x=str(x)
    x=eval(x)
    if typeOfInfo=="Money":
        infoLabel=Label(frame, text=f"Your current balance is:\n{x["money"]}", font=("Helvetica", 10), background="black", foreground="white")
        infoLabel.pack(pady=2.5)
    elif typeOfInfo=="Stocks":
        infoLabel=Label(frame, text=f"Here are your current holdings:\nApple: {x["stock1"]}\nGoogle: {x["stock2"]}\nAmazon: {x["stock3"]}\nNestle: {x["stock4"]}\nToyota: {x["stock5"]}", font=("Helvetica", 10), background="black", foreground="white")
        infoLabel.pack(pady=2.5)
    backBut=Button(frame, text="Main Menu", command=lambda: gameStart(name, win), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    backBut.pack(pady=2.5)
    frame.place(relx=0.5, rely=0.5, anchor="c")

def gameStart(name, window):
    cScreen(window)
    window.title("Main Menu")
    nameText=Label(window, text=name, font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    nameText.pack(side=TOP, anchor="e")
    window.configure(background="Black")
    mF=Frame(window, bg="black")
    s1=Button(mF, text="Apple", command=lambda: startStock(1, window, name), font=("Helvetica", 10), background="black", foreground="#A2AAAD", activebackground="black", activeforeground="#A2AAAD")
    s1.pack(pady=2.5)
    s2=Button(mF, text="Google", command=lambda: startStock(2, window, name), font=("Helvetica", 10), background="#C51C0F", foreground="#F4B400", activebackground="#C51C0F", activeforeground="#F4B400")
    s2.pack(pady=2.5)
    s3=Button(mF, text="Amazon", command=lambda: startStock(3, window, name), font=("Helvetica", 10), background="black", foreground="#FF9900", activebackground="black", activeforeground="#FF9900")
    s3.pack(pady=2.5)
    s4=Button(mF, text="Nestle", command=lambda: startStock(4, window, name), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    s4.pack(pady=2.5)
    s5=Button(mF, text="Toyota", command=lambda: startStock(5, window, name), font=("Helvetica", 10), background="#EB0A1E", foreground="white", activebackground="#EB0A1E", activeforeground="white")
    s5.pack(pady=2.5)
    bal=Button(mF, text="Check Balance", command=lambda: checkProfile("Money", window, name), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    bal.pack(pady=2.5)
    stocks=Button(mF, text="Check Stocks", command=lambda: checkProfile("Stocks", window, name), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    stocks.pack(pady=2.5)
    x=Button(mF,text="Quit", command=lambda: exitFunc(window), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    x.pack(pady=2.5)
    mF.place(relx=0.5, rely=0.5, anchor="c")

def successFulLoginSignup(name, window):
    gameStart(name, window)


def delFromLocalList(name, frame):
    import users
    cScreen(frame)
    l = users.users
    l.pop(l.index(name))
    if len(l)>1:
        with open("users.py","w") as delUser:
            delUser.write(f"users={l}")
    else:
        os.remove("users.py")
    userDeletedLabel=Label(frame, text="User has been deleted from local list successfully!\nPlease restart the game to log into another account or signup for a new account.", font=("Helvetica", 10))
    userDeletedLabel.pack()
    exitButton=Button(frame, text="Exit", command=exit, font=("Helvetica", 10))
    exitButton.pack()


def logInBackend(name, frame, passwrd, window, nameList):
    passwd = passwrd.get()
    cScreen(frame)
    with open("users.py", "w") as writeNames:
        writeNames.write(f"users = {nameList}")
    r = online.loginURL(name, passwd)
    if r == "correct password":
        successLabel = Label(frame, text="Login successful! Launching Game...", font=("Helvetica", 10), background="black", foreground="white")
        successLabel.pack(pady=2.5)
        os.rename("users.py", "users.smgf")
        window.after(3000, func=lambda: successFulLoginSignup(name, window))
    elif r == "wrong password":
        failLabel = Label(frame, text="Login Failed! Try again...", font=("Helvetica", 10), background="black", foreground="white")
        failLabel.pack(pady=2.5)
        tryAgainButton = Button(frame, text="Try Again", command=lambda: logInStart(name, frame, window, nameList), font=("Helvetica", 10), background="black", foreground="white",activebackground="black", activeforeground="white")
        tryAgainButton.pack(pady=2.5)
        forgotPassword = Button(frame, text="Forgot Password? E-mail us", command=lambda: os.system("start https://aarushiswinner.netlify.app/help"), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
        forgotPassword.pack(pady=2.5)
    elif r == "no user":
        failLabel = Label(frame, text="Login Failed! Username does not exist!", font=("Helvetica", 10), background="black", foreground="white")
        failLabel.pack(pady=2.5)
        delFromlist = Button(frame, text="Delete account from local storage?", command=lambda: delFromLocalList(name, frame), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
        delFromlist.pack(pady=2.5)
        support = Button(frame, text="Contact support", command=lambda: os.system("start https://aarushiswinner.netlify.app/help"), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
        support.pack(pady=2.5)


def logInStart(name, frame, window, lst):
    cScreen(frame)
    window.configure(background="black")
    frame.configure(background="black")
    userLabel = Label(frame, text=name, font=("Helvetica", 10), background="black", foreground="white")
    userLabel.grid(column=1, row=1)
    passwordLabel = Label(frame, text="Password:", font=("Helvetica", 10), background="black", foreground="white")
    passwordLabel.grid(column=0, row=2)
    passwordEntry = Entry(frame, width=20, show="*", background="#8A8A8A", foreground="white")
    passwordEntry.grid(column=1, row=2)
    submit = Button(frame, text="Login", command=lambda: logInBackend(name, frame, passwordEntry, window, lst), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
    window.bind("<Return>", (lambda x: logInBackend(name, frame, passwordEntry, window, lst)))
    submit.grid(column=1, row=3)


def logInGUI(signupWindow=None, frame=None, name=None):
    names = []
    if signupWindow == None:
        signupWindow = Tk()
        photo = PhotoImage(file="logo.png")
        signupWindow.wm_iconphoto(False, photo)
        signupWindow.title(" Share Market Game - Login")
        signupWindow.geometry("800x600")
        signupWindow.configure(background="black")
        frame = Frame(signupWindow, background="black")
        if name == None:
            f = os.path.isfile("users.py")
            frame.place(relx=0.5, rely=0.5, anchor="c")
            if f:
                import users
                u = users.users
                for i in u:
                    b = Button(frame, text=i, command=lambda: logInStart(i, frame, signupWindow, names), font=("Helvetica", 10), background="black", foreground="white", activebackground="black", activeforeground="white")
                    b.pack()
                    names.append(i)
                signupWindow.mainloop()
    else:
        names.append(name)
        cScreen(frame)
        signupWindow.title(" Share Market Game - Login")
        logInStart(name, frame, signupWindow, names)


def signUpStart(frame, window, username, passwrd):
    user = username.get("1.0", "end-1c")
    password = passwrd.get()
    r = online.SignUpURL(user, password)
    cScreen(frame)
    if str(r) == "Fail" or str(r) == "Failed":
        window.title(" Share Market Game - Signup Failed!")
        failedLabel = Label(frame, text="Signup failed, please try again later :)", font=("Helvetica", 10))
        failedLabel.pack()
        window.after(3000, func=window.destroy)
    elif str(r) == "Done!":
        if os.path.isfile("users.py"):
            import users
            x = users.users
            x.append(user)
            with open("users.py", "w") as s:
                s.write(f"users={x}")
        else:
            x = []
            x.append(user)
            with open("users.py", "w") as s:
                s.write(f"users={x}")
        os.rename("users.py","users.smgf")
        window.title(" Share Market Game - Signup Successful!")
        successLabel = Label(frame, text="Signup Successful! Starting game in 3 seconds!", font=("Helvetica", 10))
        successLabel.pack()
        window.after(3000, func=lambda: successFulLoginSignup(user, window))
    elif str(r) == "User exists!":
        window.title(" Share Market Game - Signup Failed!")
        failedLabel = Label(frame, text="Signup Unsuccessful! Username already exists!", font=("Helvetica", 10))
        failedLabel.pack()
        logbutton = Button(frame, text="Try different username?", command=lambda: signUpGUI(window), font=("Helvetica", 10))
        logbutton.pack()
        logbutton = Button(frame, text="Support", command=lambda: os.system("start https://aarushiswinner.netlify.app/help"), font=("Helvetica", 10))
        logbutton.pack()


def signUpGUI(win=None):
    if win!=None:
        win.destroy()
    else:
        pass
    gui = Tk(className=" Share Market Game - Signup")
    gui.geometry("800x600")
    x = Frame(gui)
    print("initialised")
    nameLabel = Label(x, text="Username: ", font=("Helvetica", 10))
    nameLabel.pack()
    nameEntry = Text(x, height=1, width=20)
    nameEntry.pack()
    passwdLabel = Label(x, text="Password: ", font=("Helvetica", 10))
    passwdLabel.pack()
    passwd = Entry(x, width=20, show="*")
    passwd.pack()
    submit = Button(x, text="Submit", activebackground="black", activeforeground="white", command=lambda: signUpStart(x, gui, nameEntry, passwd), font=("Helvetica", 10))
    submit.pack()
    x.place(relx=0.5, rely=0.5, anchor="c")
    gui.mainloop()


def mainGame():
    f=os.path.isfile("users.smgf")
    if f:
        os.rename("users.smgf","users.py")
        logInGUI()
    else:
        j=os.path.isfile("users.py")
        if j:
            logInGUI()
        else:
            signUpGUI()


if __name__ == "__main__":
    connect.connect()
    mainGame()