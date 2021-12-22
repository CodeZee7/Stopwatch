'''

This script was coded by, and belongs to:

        CodeZee - Zeeshan Ibrahim

'''

#import necessary modules
import tkinter as tk
from tkinter import *

#pillow and image must be installed by pip first
from PIL import ImageTk, Image

#timeFlow -> running clock
timeFlow=False

#create a variable for the background colour
bgColour = "#00fdcf"

#create the tkinter window
win = Tk()

win.geometry("1300x750+10+10") #size & position
win.title("Stopwatch") #window title
win.config(bg=bgColour) #colour
win.iconbitmap("stopwatchIcon.ico") #bitmap icon
win.resizable(False,False) #resizable property (not resizable)

#initialise
secs=0
minutes=0
hours=0


def updateTime():
    if (timeFlow):
        global secs,minutes,hours

        #increment seconds
        secs += 1

        #60 secs = 1 minute
        if secs > 60:
            minutes +=1
            secs = 0

        #60 minutes = 1 hour
        if minutes > 60:
            hours += 1
            minutes = 0

        #update timer label
        timerlbl.config(text=f"{hours}h:{minutes}m:{secs}s")

    #window completes after 1000 millisecs (1 second)
    win.after(1000,updateTime)


def startStopwatch():
    global timeFlow
    timeFlow = True


def stopStopwatch():
    global timeFlow
    timeFlow = False


def resetStopwatch():
    global secs,minutes,hours
    secs,minutes,hours = 0,0,0

    #update timer label
    timerlbl.config(text=f"{hours}h:{minutes}m:{secs}s")
    

def exitProgram():
    win.destroy()
    exit()


#create label with title text
titlelbl = Label(win, text="Stopwatch", font=("Arial",70,"bold"), fg="white", bg=bgColour)
titlelbl.pack()

#resize image and convert it into a PhotoImage
img = Image.open("stopwatchImage.png")
img = img.resize((500,500))
io = ImageTk.PhotoImage(img)

#create a label with the timer image and the elapsed time
timerlbl = Label(win, text=f"{hours}h:{minutes}m:{secs}s", font=("Arial",50,"bold"), fg="white", image=io, bg=bgColour, compound="center")
timerlbl.pack()

#create a frame for all the buttons
btnFrame = Frame(win, bg=bgColour)
btnFrame.pack(pady=10)

#=================================Buttons===========================================

startButton = Button(btnFrame, text="Start", font=("arial",30,"bold"), width=10, height=1, command=startStopwatch)
startButton.pack(side=LEFT, padx=5)

stopButton = Button(btnFrame, text="Stop", font=("arial",30,"bold"), width=10, height=1, command=stopStopwatch)
stopButton.pack(side=LEFT, padx=5)

resetButton = Button(btnFrame, text="Reset", font=("arial",30,"bold"), width=10, height=1, command=resetStopwatch)
resetButton.pack(side=LEFT, padx=5)

exitButton = Button(btnFrame, text="Exit", font=("arial",30,"bold"), width=10, height=1, command=exitProgram)
exitButton.pack(side=LEFT, padx=5)

updateTime()

win.mainloop()
