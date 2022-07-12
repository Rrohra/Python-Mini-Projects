from tkinter import *

root=Tk()

canvas = Canvas(root, height= 250, width=300)
canvas.pack()

blackline = canvas.create_line(0,0,200,50)
green_box= canvas.create_rectangle(25,25, 130, 270, fill="green")
red_line= canvas.create_line(0,100,210,60, fill="red")
circle = canvas.create_oval(25,25,50,50)
canvas.delete(red_line, blackline)
root.mainloop()