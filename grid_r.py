from tkinter import *

root=Tk()

label1 = Label(root, text="name", bg="red", fg="purple")
label2 = Label(root, text= "password", fg="blue", bg="yellow")

entry= Entry(root)
entry2=Entry(root)

label1.grid(row=0, column=0, sticky=E)
label2.grid(row=1, column=0)

entry.grid(row=0, column=1)
entry2.grid(row=1,column=1)

k= Checkbutton(root, text="keep me logged in")
k.grid(columnspan=2)

root.mainloop()
