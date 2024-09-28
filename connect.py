import online
from tkinter import *

x=""
def destroyFunc(window, up):
        window.destroy()
        if not up:
            print("Byyeeeeee :)")
            quit()
            return
        elif up:
            print("Starting...")
            return
def startConnection(window, lab):
    global x
    x=online.testping()
    if x=="Server is up!":
        window.title("Connected! Starting... :)")
        lab.configure(text="Server Connected! Starting in 3 seconds...")
        window.after(3100,func=lambda: destroyFunc(window, True))
    elif x=="Server is down or being updated":
        lab.configure(text="Server is down or being updated! Please try again later :)")
        window.title("Server is down or being updated")
        window.after(5100, func=lambda: destroyFunc(window, False))
    elif x=="Offline":
        lab.configure(text="No Internet. Please connect to the internet and try again :)")
        window.title("Disconnected")
        window.after(4100, func=lambda: destroyFunc(window, False))
def connect():
    global serverCon
    serverCon=Tk(className=" Share Market Game - Checking connection")
    serverCon.geometry("800x600")
    l=Label(serverCon, text="Connecting...")
    l.pack()
    photo=PhotoImage(file="logo.png")
    serverCon.wm_iconphoto(False, photo)
    serverCon.after(2000, func=lambda: startConnection(serverCon, l))
    mainloop()
    return