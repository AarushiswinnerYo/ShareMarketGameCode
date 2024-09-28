import connect
import online
from tkinter import *
import os


def cScreen(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def successFullLoginSignup(name, window):
    window.destroy()


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
    userDeletedLabel=Label(frame, text="User has been deleted from local list successfully!\nPlease restart the game to log into another account or signup for a new account.")
    userDeletedLabel.pack()
    exitButton=Button(frame, text="Exit", command=exit)
    exitButton.pack()


def logInBackend(name, frame, passwrd, window, nameList):
    passwd = passwrd.get()
    cScreen(frame)
    with open("users.py", "w") as writeNames:
        writeNames.write(f"users = {nameList}")
    r = online.loginURL(name, passwd)
    if r == "correct password":
        successLabel = Label(frame, text="Login successful! Launching Game...")
        successLabel.pack()
        window.after(3000, func=window.destroy)
    elif r == "wrong password":
        failLabel = Label(frame, text="Login Failed! Try again...")
        failLabel.pack()
        tryAgainButton = Button(frame, text="Try Again", command=lambda: logInStart(name, frame, window, nameList))
        tryAgainButton.pack()
    elif r == "no user":
        failLabel = Label(frame, text="Login Failed! Username does not exist!")
        failLabel.pack()
        delFromlist = Button(frame, text="Delete account from local storage?",
                             command=lambda: delFromLocalList(name, frame))
        delFromlist.pack()
        support = Button(frame, text="Contact support",
                         command=lambda: os.system("start https://aarushiswinner.netlify.app/help"))
        support.pack()


def logInStart(name, frame, window, lst):
    cScreen(frame)
    userLabel = Label(frame, text=name)
    userLabel.grid(column=1, row=1)
    passwordLabel = Label(frame, text="Password:")
    passwordLabel.grid(column=0, row=2)
    passwordEntry = Entry(frame, width=20, show="*")
    passwordEntry.grid(column=1, row=2)
    submit = Button(frame, text="Login", command=lambda: logInBackend(name, frame, passwordEntry, window, lst))
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
            if f:
                import users
                u = users.users
                for i in u:
                    b = Button(frame, text=i, command=lambda x=i: logInStart(i, frame, signupWindow, names))
                    b.pack()
                    names.append(i)
                frame.pack()
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
    if str(r) == "Fail":
        window.title(" Share Market Game - Signup Failed!")
        failedLabel = Label(frame, text="Signup failed, please try again later :)")
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
        window.title(" Share Market Game - Signup Successful!")
        successLabel = Label(frame, text="Signup Successful! Starting game in 3 seconds!")
        successLabel.pack()
        window.after(3000, func=window.destroy)
    elif str(r) == "User exists!":
        window.title(" Share Market Game - Signup Failed!")
        failedLabel = Label(frame, text="Signup Unsuccessful! Username already exists!")
        failedLabel.pack()
        logbutton = Button(frame, text="Try different username?", command=lambda: signUpGUI(window))
        logbutton.pack()
        logbutton = Button(frame, text="Support", command=lambda: os.system("start https://aarushiswinner.netlify.app/help"))
        logbutton.pack()


def signUpGUI(win=None):
    if win!=None:
        win.destroy()
    else:
        pass
    gui = Tk(className=" Share Market Game - Signup")
    photo = PhotoImage(file="logo.png")
    gui.geometry("800x600")
    gui.wm_iconphoto(False, photo)
    x = Frame(gui)
    nameLabel = Label(x, text="Username: ")
    nameLabel.grid(column=0, row=1)
    nameEntry = Text(x, height=1, width=20)
    nameEntry.grid(column=1, row=1)
    passwdLabel = Label(x, text="Password: ")
    passwdLabel.grid(column=0, row=2)
    passwd = Entry(x, width=20, show="*")
    passwd.grid(column=1, row=2)
    submit = Button(x, text="Submit", activebackground="black", activeforeground="white",
                    command=lambda: signUpStart(x, gui, nameEntry, passwd))
    submit.grid(column=1, row=3)
    x.pack()
    gui.mainloop()


def mainGame():
    try:
        import users
    except ModuleNotFoundError:
        signUpGUI()
    else:
        logInGUI()


if __name__ == "__main__":
    connect.connect()
    print("hello")
    mainGame()
