#way1
#from tkinter import *
#root = Tk()


#def fucn_i():
 #   label= Label(root, text="my name is rohit", fg="red")
  #  label.grid(row=2, column=2)

#button1 = Button(root, text="sold", command =fucn_i)
#button1.grid(row=25,column=25)

#root.mainloop()




#way 2
from tkinter import *

root= Tk()
def printname(event):
    print("hello rohit")
button_1 = Button(root, text = "print my name")
button_1.bind("<Button-1>", printname)
button_1.pack()

root.mainloop()