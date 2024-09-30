import time
import connect
import online
from tkinter import *
import os


def cScreen(frame):
    for widget in frame.winfo_children():
        widget.destroy()

stockNames=["Apple", "Google", "Amazon", "Nestle", "Toyota"]

def startStock(stock, win,name):
    cScreen(win)
    nameText=Label(win, text=name)
    nameText.pack(side=TOP, anchor="w")
    win.title(stockNames[stock-1])
    frame=Frame(win)
    backBut=Button(frame, text="Main Menu", command=lambda: gameStart(name, win))
    backBut.pack()
    x=Button(frame,text="Quit", command=exit)
    x.pack()
    frame.place(relx=0.5, rely=0.5, anchor="c")

def gameStart(name, window):
    cScreen(window)
    window.title("Main Menu")
    nameText=Label(window, text=name)
    nameText.pack(side=TOP, anchor="w")
    mF=Frame(window)
    s1=Button(mF, text="Apple", command=lambda: startStock(1, window, name), font=("Helvetica", 10))
    s1.pack(pady=1)
    s2=Button(mF, text="Google", command=lambda: startStock(2, window, name), font=("Helvetica", 10))
    s2.pack(pady=1)
    s3=Button(mF, text="Amazon", command=lambda: startStock(3, window, name), font=("Helvetica", 10))
    s3.pack(pady=1)
    s4=Button(mF, text="Nestle", command=lambda: startStock(4, window, name), font=("Helvetica", 10))
    s4.pack(pady=1)
    s5=Button(mF, text="Toyota", command=lambda: startStock(5, window, name), font=("Helvetica", 10))
    s5.pack(pady=1)
    bal=Button(mF, text="Check Balance", command=lambda: print("Check Balance..."), font=("Helvetica", 10))
    bal.pack(pady=1)
    stocks=Button(mF, text="Check Stocks", command=lambda: print("Check Stocks..."), font=("Helvetica", 10))
    stocks.pack(pady=1)
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
        successLabel = Label(frame, text="Login successful! Launching Game...", font=("Helvetica", 10))
        successLabel.pack()
        os.rename("users.py", "users.smgf")
        window.after(3000, func=lambda: successFulLoginSignup(name, window))
    elif r == "wrong password":
        failLabel = Label(frame, text="Login Failed! Try again...", font=("Helvetica", 10))
        failLabel.pack()
        tryAgainButton = Button(frame, text="Try Again", command=lambda: logInStart(name, frame, window, nameList), font=("Helvetica", 10))
        tryAgainButton.pack()
    elif r == "no user":
        failLabel = Label(frame, text="Login Failed! Username does not exist!", font=("Helvetica", 10))
        failLabel.pack()
        delFromlist = Button(frame, text="Delete account from local storage?", command=lambda: delFromLocalList(name, frame), font=("Helvetica", 10))
        delFromlist.pack()
        support = Button(frame, text="Contact support", command=lambda: os.system("start https://aarushiswinner.netlify.app/help"), font=("Helvetica", 10))
        support.pack()


def logInStart(name, frame, window, lst):
    cScreen(frame)
    userLabel = Label(frame, text=name, font=("Helvetica", 10))
    userLabel.grid(column=1, row=1)
    passwordLabel = Label(frame, text="Password:", font=("Helvetica", 10))
    passwordLabel.grid(column=0, row=2)
    passwordEntry = Entry(frame, width=20, show="*")
    passwordEntry.grid(column=1, row=2)
    submit = Button(frame, text="Login", command=lambda: logInBackend(name, frame, passwordEntry, window, lst), font=("Helvetica", 10))
    submit.grid(column=1, row=3)


def logInGUI(signupWindow=None, frame=None, name=None):
    names = []
    if signupWindow == None:
        signupWindow = Tk()
        photo = PhotoImage(file="logo.png")
        signupWindow.wm_iconphoto(False, photo)
        signupWindow.title(" Share Market Game - Login")
        signupWindow.geometry("800x600")
        frame = Frame(signupWindow)
        if name == None:
            f = os.path.isfile("users.py")
            frame.place(relx=0.5, rely=0.5, anchor="c")
            if f:
                import users
                u = users.users
                for i in u:
                    b = Button(frame, text=i, command=lambda: logInStart(i, frame, signupWindow, names), font=("Helvetica", 10))
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
        signUpGUI()


if __name__ == "__main__":
    connect.connect()
    mainGame()