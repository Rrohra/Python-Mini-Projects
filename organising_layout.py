from tkinter import *

root = Tk()

topFrame  =Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side="bottom")
middleFrame =Frame(root)
middleFrame.pack(side="left")


label1=Label(bottomFrame, text = "whats up rohra", fg= "pink", bg = "black")
label1.pack()


button = Button(middleFrame , text="button 1", fg="red") #fore grounf = fg
button2 = Button(middleFrame , text="button 2", fg="blue") #fore grounf = fg
button3 = Button(bottomFrame , text="button 3", fg="orange") #fore grounf = fg

button.pack(side="left")
button2.pack(side="right")
button3.pack(side="left")


root.mainloop()
