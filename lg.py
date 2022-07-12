from tkinter import *


root = Tk()
root.title("LOG-IN")
f = Frame(root, height=400, width=400)
f.pack()
f.propagate(0)


lx = Label(f, text='User Name :')
ly = Label(f, text='Password :')
ex = Entry(f, width=5, fg='black', bg='gray', font=('arial', 20))
ey = Entry(f, width=5, fg='black', bg='gray', show='*', font=('arial', 20))


def log():
    a = ex.get()
    b = ey.get()

    if (a == 'admin') and (b == 'admin'):
        print("successful")
    else:
        print("invalid")


b = Button(f, text='Log-in', command=log)

b.place(x= 200, y=200)
lx.place(x=1, y=20)
ex.place(x=150, y=20)
ly.place(x=1, y=100)
ey.place(x=150, y=100)

root.mainloop()