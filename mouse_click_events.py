from tkinter import *

root =Tk()

def leftclick(event):
    print("left")

def rightclick(event):
    print("right click")

def middleclick(event):
    print("middle")

frame= Frame(root, width =300, height= 250)
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)
frame.pack()

root.mainloop()