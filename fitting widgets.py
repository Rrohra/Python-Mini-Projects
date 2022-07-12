from tkinter import *

root = Tk()


bottomFrame  =Frame(root)
bottomFrame.pack(side="bottom")


label1 = Label(bottomFrame , text="hey wassup", fg= "red", bg="green")
label1.pack()
label2 = Label(root , text="i am growing", fg= "orange", bg="purple")
label2.pack(fill=X)
label3 = Label(root , text="i am growing in  y direction", fg="brown", bg="yellow")
label3.pack(side=RIGHT,  fill=Y)




root.mainloop()