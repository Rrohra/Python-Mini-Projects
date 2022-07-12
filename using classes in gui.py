from tkinter import *

class rohra:
    def __init__(self, master):
        frame= Frame(master)
        frame.pack()

        self.printbutton = Button(frame, text="printthis", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton= Button(frame,text="quit", command=frame.quit)
        self.quitbutton.pack()

    def printmessage(self):
        print("hey rohit rohra do u love kanksha salvi?")

root= Tk()
r= rohra(root)
root.mainloop()