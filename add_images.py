from tkinter import *

root=Tk()

image= PhotoImage(file="rohit.png")
label =Label(root, Image=image)
label.pack()

root.mainloop()