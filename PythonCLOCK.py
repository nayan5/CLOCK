
#PYTHON PROJECT TO MAKE A CLOCK

from tkinter import *   # From tkinter import all

from tkinter.ttk import * # for using Label on line 21

from time import strftime # import Time

root = Tk() #create UI for clock(creating tkinter window)
root.title("My Clock") # Title = My Clock


def time():
    string = strftime('%H:%M:%S %p')  #store time in string
    label.config(text=string)   
    label.after(3000,time)  #call time function on every 3sec


# Download Font : https://www.dafont.com/ds-digital.font

label = Label(root,font=("ds-digital",80),background = "black", foreground = "cyan")


label.pack(anchor="center") 
"""
Anchors are used to define where text is positioned relative to a reference point.

Here is list of possible constants, which can be used for Anchor attribute.

NW
N
NE
W
CENTER
E
SW
S
SE
"""
time()

mainloop()

